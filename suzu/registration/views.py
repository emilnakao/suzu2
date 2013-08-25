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
from braces.views import LoginRequiredMixin, CsrfExemptMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView
from django.views.generic.base import TemplateView
from .models import Yokoshi
from .forms import YokoshiForm


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