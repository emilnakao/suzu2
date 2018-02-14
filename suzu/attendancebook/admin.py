# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.http import HttpResponse
from .models import Country, State, City, Yokoshi, Han, Regional, EventType, Presence, Event

# Register your models here.


def export_yokoshi_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=suzu_yokoshi.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"Nome"),
        smart_str(u"Nucleo"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.complete_name),
            smart_str(obj.han.name),
        ])
    return response


export_yokoshi_csv.short_description = u"Exportar CSV"

# def merge_selected_objects(modeladmin, request, queryset):
#     selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
#     ct = ContentType.objects.get_for_model(queryset.model)
#     return HttpResponseRedirect("/attendancebook/merge/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))
#
# merge_selected_objects.short_description = u"Unificar registros"


class YokoshiAdmin(ModelAdmin):
    """
    Administration interface for yokoshi.
    """
    # form = autocomplete.modelform_factory(Yokoshi)
    search_fields = ['complete_name', 'is_mikumite']
    list_display = ('complete_name', 'is_mtai', 'is_ossuewanin', 'is_mikumite', 'is_inactive')
    list_filter = ('han', 'is_mtai', 'is_ossuewanin', 'is_mikumite', 'is_inactive')
    actions = [export_yokoshi_csv]


class PresenceAdmin(ModelAdmin):
    search_fields = ['yokoshi__complete_name']
    list_display = ('yokoshi', 'event', 'begin_date_time')
    list_filter = ('begin_date_time', 'is_first_time')


class EventAdmin(ModelAdmin):
    search_fields = ['event_type__name']
    list_display = ('event_type', 'begin_date_time')
    list_filter = ('event_type', 'begin_date_time')


class HanAdmin(ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'regional', 'additional_information')
    list_filter = ['regional']


admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Yokoshi, YokoshiAdmin)
admin.site.register(Han, HanAdmin)
admin.site.register(Regional)
admin.site.register(EventType)
admin.site.register(Presence, PresenceAdmin)
admin.site.register(Event, EventAdmin)
