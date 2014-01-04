"""
Copyright (c) 2013 The Suzu Team

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
permit persons to whom the Software is furnished to do so, subject to the following 
conditions:

The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE
"""
from datetime import datetime
from braces.views import LoginRequiredMixin, CsrfExemptMixin, PermissionRequiredMixin
from django.core import serializers
from django.db import connection
from django.http import HttpResponse

from django.utils.translation import ugettext
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.base import TemplateView
from .models import Yokoshi, Presence, Event
from .forms import YokoshiForm
from .simplejson import json_response_from


class RegistrationHomeView(LoginRequiredMixin, TemplateView):
    """
    Home screen; easy access to all registration screens
    """
    template_name = 'registration/home.html'


class YokoshiCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    see: http://django-braces.readthedocs.org/en/latest/index.html
    """
    model = Yokoshi
    form_class = YokoshiForm
    permission_required = 'registration.yokoshi_create'


class YokoshiListView(LoginRequiredMixin, ListView):
    """

    """
    model = Yokoshi

    #def get_queryset(self):
    # return Yokoshi.objects.filter(complete_name__icontains=self.args[0])


class PresenceConfirmationView(DetailView):

    """
    View for presence confirmation. Displays a notification message saying that the presence was successfully saved.
    """
    model = Yokoshi
    template_name = 'dummy.html'

    def get_object(self):
        # Call the superclass
        whoId = self.request.GET["yokoshi"]
        who = Yokoshi.objects.get(pk=whoId)
        eventId = self.request.GET['current_event']
        event = Event.objects.get(pk=eventId)
        when = datetime.now()
        object = Presence.confirmPresence(who=who, event=event, arrival=when)
        self.request.session['notification_message'] = who.complete_name + ' ' + ugettext(
            "user_info.is_present_in.msg") + ' ' + event.__unicode__()
        # Return the object
        return who


class PresenceCancellationView(DetailView):
    """
    View for presence cancellation. Displays a notification message saying that the presence was cancelled.
    """
    model = Yokoshi
    template_name = 'dummy.html'

    def get_object(self):
        # Call the superclass
        whoId = self.request.GET["yokoshi"]
        who = Yokoshi.objects.get(pk=whoId)
        eventId = self.request.GET['current_event']
        event = Event.objects.get(pk=eventId)
        object = Presence.cancelPresence(who=who, event=event)
        self.request.session['notification_message'] = who.complete_name + ' ' + ugettext(
            "user_info.is_present_in.msg") + ' ' + event.__unicode__()
        # Return the object
        return who


# TODO: passar para modulo reports
def generate_report(request):
    cursor = connection.cursor()
    cursor.execute('SELECT p.id, y.complete_name as name, h.name as han from registration_presence p inner join registration_yokoshi y on y.id = p.yokoshi_id inner join registration_han h on h.id = y.han_id where p.event_id = %s order by y.complete_name asc, h.name asc', [request.GET['event']])
    comments = dictfetchall(cursor)
    # comments = Presence.objects.raw('SELECT p.id, y.complete_name as name, h.name as han from registration_presence p inner join registration_yokoshi y on y.id = p.yokoshi_id inner join registration_han h on h.id = y.han_id where p.event_id = %s order by y.complete_name asc, h.name asc', [request.GET['event']])
    return json_response_from(comments)

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]