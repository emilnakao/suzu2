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
import datetime
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import models
from model_utils import Choices
from model_utils.managers import PassThroughManager
from model_utils.models import TimeStampedModel
from .querysets import YokoshiQuerySet


class Regional(TimeStampedModel):
    """
    Represents a physical mahikari dojo. It can be associated to a bigger dojo;
    in this case, it will indicate the relationship with parent_regional
    @since 1.0
    """

    class Meta:
        verbose_name = _('regional')
        verbose_name_plural = _('regionals')

    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name=_('Regional|name'))
    parent_regional = models.ForeignKey('Regional', null=True, blank=True, default=None,
                                        verbose_name=_('Regional|parent_regional'))

    def __unicode__(self):
        return u'%s' % self.name


class Han(TimeStampedModel):
    """
    Representa um nucleo (han)
    """

    class Meta:
        verbose_name = _('han')
        verbose_name_plural = _('hans')

    name = models.CharField(max_length=100, null=True, blank=True, unique=True, db_index=True,
                            verbose_name=_('Han|name'))
    regional = models.ForeignKey(Regional, verbose_name=_('Han|regional'), null=True, blank=True, default=None, db_index=True)
    additional_information = models.TextField(max_length=20000, null=True, blank=True,
                                              verbose_name=_('Han|additional_information'))

    def __unicode__(self):
        return u'%s' % self.name


class Yokoshi(TimeStampedModel):
    """
    A yokoshi registry. Contains basic information for person identification,
    search, localization and contact. Can be linked with a django User too.
    """
    OMITAMA_LEVEL = Choices(('none', _('none_omitama_level')), ('basic', _('basic_omitama_level')),
                            ('intermediate', _('intermediate_omitama_level')),
                            ('advanced', _('advanced_omitama_level')))

    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, db_index=True, verbose_name=_('Yokoshi|user'))
    complete_name = models.CharField(max_length=500, db_index=True, verbose_name=_('Yokoshi|complete_name'))
    phonetic_name = models.CharField(max_length=500, null=True, blank=True, db_index=True, editable=False,
                                     verbose_name=('Yokoshi|phonetic_name'))
    email = models.EmailField(null=True, blank=True, verbose_name=_('Yokoshi|email'))
    phone = models.CharField(max_length=40, null=True, blank=True, verbose_name=_('Yokoshi|phone'))
    address = models.ForeignKey("Address", null=True, blank=True, db_index=True, verbose_name=_('Yokoshi|address'))
    additional_information = models.TextField(max_length=30000, null=True, blank=True,
                                              verbose_name=_('Yokoshi|additional_information'))
    birthday = models.DateField(null=True, blank=True, verbose_name=_('Yokoshi|birthday'))
    is_inactive = models.BooleanField(default=False, verbose_name=_('Yokoshi|is_inactive'))
    seminary_number = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('Yokoshi|seminary_number'))
    han = models.ForeignKey(Han, null=True, blank=True, db_index=True, verbose_name=_('Yokoshi|han'))
    is_mtai = models.BooleanField(default=False, verbose_name=_('Yokoshi|is_mtai'))
    is_ossuewanin = models.BooleanField(default=False, verbose_name=_('Yokoshi|is_ossuewanin'))
    is_mikumite = models.BooleanField(default=False, verbose_name=_('Yokoshi|is_mikumite'))
    omitama_level = models.CharField(choices=OMITAMA_LEVEL, default=OMITAMA_LEVEL.none, max_length=50)
    indication = models.ManyToManyField("Yokoshi", null=True, blank=True, db_index=True, verbose_name=_('Yokoshi|indication'))

    class Meta:
        verbose_name = _('yokoshi')
        verbose_name_plural = _('yokoshis')

    def __unicode__(self):
        return u'%s' % self.complete_name

    # Allows more friendly query set filters (see django-model-utils docs):
    objects = PassThroughManager.for_queryset_class(YokoshiQuerySet)()

    def save(self, force_insert=False, force_update=False, using=None):
        """
        Before saving, updates the phonetic representation of complete_name
        """
        if self.han is None:
            self.han = Han.objects.get_or_create(name='Desconhecido')[0]

        super(Yokoshi, self).save(force_insert, force_update, using)


class Country(TimeStampedModel):
    """
    Simple entity to represent countries. Should be completed according to necessity.
    """
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name=_('Country|name'))

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')

    def __unicode__(self):
        return u'%s' % (self.name)


class State(TimeStampedModel):
    """
    Simple entity to represent states (or provinces, according to the country).
    Should be completed according to necessity.
    """

    class Meta:
        unique_together = ('name', 'country',)
        verbose_name = _('state')
        verbose_name_plural = _('states')

    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name=_('State|name'))
    country = models.ForeignKey(Country, db_index=True, verbose_name=_('State|country'))

    def __unicode__(self):
        return u'%s' % (self.name)


class City(TimeStampedModel):
    """
    Simple entity to represent cities. Should be completed according to necessity.
    """

    class Meta:
        unique_together = ('name', 'state',)
        verbose_name = _('city')
        verbose_name_plural = _('cities')

    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name=_('City|name'))
    state = models.ForeignKey(State, db_index=True, verbose_name=_('City|state'))

    def __unicode__(self):
        return u'%s' % (self.name)


class Neighborhood(TimeStampedModel):
    """
    Simple entity to represent neighborhoods. Should be completed according to necessity.
    """

    class Meta:
        unique_together = ('name', 'city',)
        verbose_name = _('neighborhood')
        verbose_name_plural = _('neighborhoods')

    name = models.CharField(max_length=100, db_index=True, verbose_name=_('Neighborhood|name'))
    city = models.ForeignKey(City, null=True, blank=True, db_index=True, verbose_name=_('Neighborhood|city'))

    def __unicode__(self):
        return u'%s' % (self.name)


class Address(TimeStampedModel):
    """
    Basic address entity. Should be completed according to necessity.
    """

    class Meta:
        unique_together = ('street_name', 'house_number', 'neighborhood')
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    street_name = models.CharField(max_length=500, null=True, blank=True, db_index=True,
                                   verbose_name=_('Address|street_name'))
    house_number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Address|house_number'))
    zip_code = models.IntegerField(max_length=12, null=True, blank=True, verbose_name=_('Address|zip_code'))
    neighborhood = models.ForeignKey(Neighborhood, null=True, blank=True, db_index=True,
                                     verbose_name=_('Address|neighborhood'))
    additional_information = models.TextField(max_length=2000, null=True, blank=True,
                                              verbose_name=_('Address|additional_information'))

    def __unicode__(self):
        return u'%s %s' % (self.street_name, self.house_number)

#######################
# CHECKIN DOMAIN
#######################


class EventType(models.Model):
    """
    An event type represents a category of event that can be
    repeated one or more times. The event type is used to categorize events,
    and does not contain information about when it happened (This is a responsibility
    of the Event class).

    Examples of event types:

    * Monthly Ceremony (It's just a description; we will create,
      for example, an event of type 'Monthly Ceremony' each month.
    * Class Meeting
    * Quarter Business Meeting
    * Annual Conference
    """

    class Meta:
        verbose_name = _('event_type')
        verbose_name_plural = _('event_types')

    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name=_('EventType|name'))
    additional_information = models.TextField(max_length=30000, blank=True, null=True, verbose_name=('EventType|additional_information'))

    def __unicode__(self):
        return self.name


class Event(models.Model):
    """

    """
    class Meta:
        unique_together = ("event_type", "begin_date_time")
        verbose_name = _('event')
        verbose_name_plural = _('events')

    event_type = models.ForeignKey(EventType, db_index=True, verbose_name=_('Event|event_type'))
    begin_date_time = models.DateTimeField(verbose_name=_('Event|begin_date_time'))
    details = models.CharField(max_length=20000, null=True, blank=True, verbose_name=_('Event|details'))

    def __unicode__(self):
        return self.event_type.name


class Presence(models.Model):

    class Meta:
        verbose_name = _('presence')
        verbose_name_plural = _('presences')

    event = models.ForeignKey(Event, db_index=True, verbose_name=_('Presence|event'))
    begin_date_time = models.DateTimeField(null=True, verbose_name=_('Presence|begin_date_time'))
    yokoshi = models.ForeignKey(Yokoshi, db_index=True, verbose_name=_('Presence|yokoshi'))
    additional_information = models.TextField(max_length=2000, verbose_name=_('Presence|additional_information'))
    is_first_time = models.BooleanField(default=False, verbose_name=_('Presence|is_first_time'))

    @classmethod
    def confirmPresence(cls, who, event, arrival, first_time=False):
        """
        Confirms the presence of a Person. The key arguments are who and event, which are considered unique in the db.
        @param who a Person object to be present at the event
        @param event an Event instance, which the user is attending
        @return the new presence instance, retrieved from the db or saved in case it didn't exists
        """
        used_arrival = arrival or datetime.now()
        presence = Presence.objects.get_or_create(event=event, yokoshi=who, is_first_time=first_time)[0]
        if presence.begin_date_time is None:
            presence.begin_date_time = used_arrival

        presence.save()
        return presence

    @classmethod
    def cancelPresence(cls, who, event):
        """
        Cancels the presence of a Person.
        """

        presence = Presence.objects.get(event=event, yokoshi=who)
        presence.delete()

    def __unicode__(self):
        return u'%s em %s (%s)' % (self.yokoshi, self.event, self.begin_date_time)