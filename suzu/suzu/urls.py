"""suzu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from tastypie.api import Api

from attendancebook.api.resources import HanResource, ReadOnlyHanResource, YokoshiResource, EventTypeResource, \
    EventResource, \
    PresenceCountResource, PresenceResource

from attendancebook.views import YokoshiListView, RegistrationHomeView, PresenceConfirmationView, \
    singleevent_report, PresenceCancellationView, single_event_excel, yokoshihistory_report, mikumite_report, \
    mikumite_excel, inform_yokoshi_update, update_han, find_or_create_event_for_today

v1_api = Api(api_name='v1')
v1_api.register(HanResource())
v1_api.register(ReadOnlyHanResource())
v1_api.register(YokoshiResource())
v1_api.register(EventTypeResource())
v1_api.register(EventResource())
v1_api.register(PresenceCountResource())
v1_api.register(PresenceResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # urls do tastypie; api REST
    url(r'^api/', include(v1_api.urls)),

    url(r'^yokoshi/list$', YokoshiListView.as_view(), "yokoshilist"),
    url(r'^home$', RegistrationHomeView.as_view(), "registrationhome"),
    url(r'^confirm_presence/$', PresenceConfirmationView.as_view(), "confirm_presence"),
    url(r'^cancel_presence/$', PresenceCancellationView.as_view(), "cancel_presence"),
    url(r'^presence_by_event/$', singleevent_report),
    url(r'^presence_by_event_excel/$', single_event_excel),
    url(r'^yokoshi_history/$', yokoshihistory_report),
    url(r'^mikumite_report/$', mikumite_report),
    url(r'^mikumite_excel/$', mikumite_excel),
    url(r'^inform_yokoshi_update/$', inform_yokoshi_update),
    url(r'^update_han/$', update_han),
    url(r'^find_or_create_event_for_today/$', find_or_create_event_for_today),
]
