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

from django.conf.urls import patterns, url
from .views import YokoshiCreateView, RegistrationHomeView, YokoshiListView, PresenceConfirmationView, PresenceCancellationView, singleevent_report, yokoshihistory_report, mikumite_report, \
    inform_yokoshi_update, single_event_excel, mikumite_excel, update_han

urlpatterns = patterns('',
                       url(r'^yokoshi/create$', YokoshiCreateView.as_view(), name="yokoshicreate"),
                       url(r'^yokoshi/list$', YokoshiListView.as_view(), name="yokoshilist"),
                       url(r'^home$', RegistrationHomeView.as_view(), name="registrationhome"),
                       url(r'^confirm_presence/$', PresenceConfirmationView.as_view(), name="confirm_presence"),
                       url(r'^cancel_presence/$', PresenceCancellationView.as_view(), name="cancel_presence"),
                       url(r'^presence_by_event/$', singleevent_report),
                       url(r'^presence_by_event_excel/$', single_event_excel),
                       url(r'^yokoshi_history/$', yokoshihistory_report),
                       url(r'^mikumite_report/$', mikumite_report),
                       url(r'^mikumite_excel/$', mikumite_excel),
                       url(r'^inform_yokoshi_update/$', inform_yokoshi_update),
                       url(r'^update_han/$', update_han),
)