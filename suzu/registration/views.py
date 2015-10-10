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
from .models import Yokoshi, Presence, Event, Han
from .forms import YokoshiForm
from .simplejson import json_response_from
import json
import xlsreports


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
        firstTime = self.request.GET['is_first_time'] in ['true', 'True']
        event = Event.objects.get(pk=eventId)
        when = datetime.now()
        object = Presence.confirmPresence(who=who, event=event, arrival=when, first_time=firstTime)
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
def singleevent_report(request):
    """
    will be deprecated soon
    :param request:
    :return:
    """
    cursor = connection.cursor()
    cursor.execute(
        'SELECT y.complete_name as nome, h.name as han, y.is_mikumite as mikumite, p.is_first_time as firsttime from registration_presence p inner join registration_yokoshi y on y.id = p.yokoshi_id inner join registration_han h on h.id = y.han_id where p.event_id = %s order by h.name asc, y.complete_name asc',
        [request.GET['event']])
    comments = dictfetchall(cursor)
    # comments = Presence.objects.raw('SELECT p.id, y.complete_name as name, h.name as han from registration_presence p inner join registration_yokoshi y on y.id = p.yokoshi_id inner join registration_han h on h.id = y.han_id where p.event_id = %s order by y.complete_name asc, h.name asc', [request.GET['event']])
    return json_response_from(comments)


def single_event_excel(request):
    """

    :param request:
    :return:
    """
    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=relatorio_evento.xls'
    workbook = xlsreports.single_event_report(long(request.GET['event']))
    workbook.save(response)
    return response


def yokoshihistory_report(request):
    """
    will be deprecated soon
    :param request:
    :return:
    """
    yokoshiId = request.GET['yokoshi']
    intervalStart = request.GET['start']
    intervalEnd = request.GET['end']

    cursor = connection.cursor()
    cursor.execute(
        'select et.name as eventtype, e.begin_date_time as begindate from registration_presence p inner join registration_event e on p.event_id = e.id inner join registration_eventtype et on et.id = e.event_type_id where p.yokoshi_id = %s and p.begin_date_time >= %s and p.begin_date_time <= %s',
        [yokoshiId, intervalStart, intervalEnd])
    comments = dictfetchall(cursor)
    return json_response_from(comments)


def mikumite_report(request):
    """
    will be deprecated soon
    :param request:
    :return:
    """
    intervalStart = request.GET['start']
    intervalEnd = request.GET['end']

    cursor = connection.cursor()
    cursor.execute((
        "select row_number() over() as resultnumber, "
        "y.complete_name as mikumite_name, "
        "coalesce(y.email, ' ') as email, "
        "coalesce(y.phone, ' ') as phone, "
        "coalesce(indication.complete_name, ' ') as indication_name, "
        "coalesce(indicationhan.name, ' ') as indication_han_name, "
        "count(p.id) as number_presences "
        "from registration_presence p "
        "inner join registration_yokoshi y on y.id = p.yokoshi_id "
        "left outer join registration_yokoshi indication on indication.id = y.indication_id "
        "left outer join registration_han indicationhan on indicationhan.id = indication.han_id "
        "where y.is_mikumite = true "
        "and p.begin_date_time >= %s "
        "and p.begin_date_time <= %s"
        "group by y.complete_name, y.email, y.phone, indication.complete_name, indicationhan.name "
        "order by y.complete_name asc"
        ""
    ), [intervalStart, intervalEnd]
    )

    results = dictfetchall(cursor)
    return json_response_from(results)


def mikumite_excel(request):
    """

    :param request:
    :return:
    """
    intervalStart = request.GET['start']
    intervalEnd = request.GET['end']

    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=relatorio_evento.xls'
    workbook = xlsreports.mikumite_report(intervalStart, intervalEnd)
    workbook.save(response)
    return response


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def inform_yokoshi_update(request):
    received_json = json.loads(request.body)
    yokoshi_list = json.loads(received_json['selectedYokoshis'])

    for yokoshi_id in yokoshi_list:
        Yokoshi.objects.filter(pk=yokoshi_id).update(last_registration_update=datetime.now())

    return HttpResponse('')

def update_han(request):
    yokoshi_id = request.GET['yokoshi_id']
    han_id = request.GET['han_id']

    new_han = Han.objects.get(pk=han_id)
    yokoshi = Yokoshi.objects.filter(pk=yokoshi_id).update(han = new_han)

    return HttpResponse('')




