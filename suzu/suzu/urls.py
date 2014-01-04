from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration import urls as registrationurls
from .settings import commons
from registration.api import HanResource, YokoshiResource, ReadOnlyHanResource, EventTypeResource, EventResource, PresenceCountResource, PresenceByEventResource
from .views import HomeView, route_request

admin.autodiscover()

from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(HanResource())
v1_api.register(ReadOnlyHanResource())
v1_api.register(YokoshiResource())
v1_api.register(EventTypeResource())
v1_api.register(EventResource())
v1_api.register(PresenceCountResource())
v1_api.register(PresenceByEventResource())

urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name='home'),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # redireciona requests a templates/<arquivo> para o arquivo.html propriamente dito
                       url(r'^templates/(?P<path>.*)', route_request),

                       # Login Screen
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', dict(template_name='login.html', ),
                           name='login', ),

                       # Logout Screen
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
                           dict(template_name='logout.html', ), name='logout', ),

                       # Redirecting profile to home
                       url(r'^accounts/profile/$', HomeView.as_view(), name='homeprofile', ),

                       # Required to make static serving work
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': commons.STATIC_ROOT}),

                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^registration/', include(registrationurls)),

                        # urls do tastypie; api REST
                       url(r'^api/', include(v1_api.urls)),
)
