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
from tastypie import fields, authorization
from tastypie.authorization import Authorization, ReadOnlyAuthorization
from tastypie.constants import ALL_WITH_RELATIONS, ALL
from tastypie.fields import ForeignKey
from tastypie.resources import ModelResource
from tastypie.validation import Validation
from .models import Han, Yokoshi, EventType, Event, Presence


class HanResource(ModelResource):
    class Meta:
        queryset = Han.objects.all()
        resource_name = 'han'


class ReadOnlyHanResource(ModelResource):
    class Meta:
        queryset = Han.objects.all()
        resource_name = 'han_read_only'

    def obj_create(self):
        raise Exception("Permission denied")


class YokoshiResource(ModelResource):
    han = fields.ToOneField(ReadOnlyHanResource, 'han', full=True, null=True, readonly=True)

    class Meta:
        queryset = Yokoshi.objects.all()
        resource_name = 'yokoshi'
        authorization = Authorization()
        filtering = {'complete_name': ['iregex'], }
        ordering = ['complete_name']
        validation = Validation()
        always_return_data = True


class EventTypeResource(ModelResource):
    class Meta:
        queryset = EventType.objects.all()
        resource_name = 'event_type'
        authorization = Authorization()


class EventResource(ModelResource):
    event_type = fields.ForeignKey(EventTypeResource, 'event_type', full=True)

    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        authorization = Authorization()
        filtering = {'begin_date_time': ALL, 'event_type': ALL_WITH_RELATIONS, "id":ALL}


class PresenceResource(ModelResource):
    yokoshi = fields.ToOneField(YokoshiResource, 'yokoshi', full=True, null=True, readonly=True)
    event = ForeignKey(EventResource, "event")

    class Meta:
        queryset = Presence.objects.order_by('-begin_date_time')
        resource_name = 'presence'
        authorization = Authorization()
        filtering = {'event': ALL_WITH_RELATIONS}
        limit = 0


class PresenceCountResource(ModelResource):
    # Precisamos mostrar na tela a qual nucleo pertence a pessoa
    han = fields.ToOneField(ReadOnlyHanResource, 'han', full=True, null=True, readonly=True)

    """
    Returns an additional column in person rows, telling how many presences the user has in the event whose id is passed
    """
    presence_count = fields.IntegerField(attribute="presence_count", default=0, readonly=True)
    event_id = 0

    class Meta:
        resource_name = 'presence_count'
        queryset = Yokoshi.objects.all()
        #        authentication = BasicAuthentication()
        authorization = ReadOnlyAuthorization()
        allowed_methods = ['get']
        filtering = {
            "complete_name": ['icontains', 'iregex', 'regex'],
        }

    def obj_get_list(self, bundle, **kwargs):
        # override default implementation
        event_id = bundle.request.GET['event_id']
        self._meta.queryset = Yokoshi.objects.extra(select={
            'presence_count': 'select count(p) from registration_presence p where p.yokoshi_id = registration_yokoshi.id and p.event_id=%s'},
                                                    select_params=[event_id]).order_by('complete_name')

        return super(PresenceCountResource, self).obj_get_list(bundle, **kwargs)