from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration import urls as registrationurls
from .settings import commons
from .views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name='home'),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Login Screen
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', dict(template_name='login.html', ),
                           name='login', ),

                       # Logout Screen
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
                           dict(template_name='logout.html', ), name='logout', ),

                        # Required to make static serving work
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': commons.STATIC_ROOT}),

                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^registration/', include(registrationurls)),
)
