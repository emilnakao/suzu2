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
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Country, State, Address, City, Neighborhood, Yokoshi, Han, Regional, EventType, Presence, Event


class YokoshiAdmin(ModelAdmin):
    """
    Administration interface for yokoshi.
    """
    search_fields = ['complete_name', 'is_mikumite']
    list_display = ('complete_name', 'is_mtai', 'is_ossuewanin', 'is_mikumite', 'is_inactive')
    list_filter = ('is_mtai', 'is_ossuewanin', 'is_mikumite', 'is_inactive')

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Address)
admin.site.register(Neighborhood)
admin.site.register(Yokoshi, YokoshiAdmin)
admin.site.register(Han)
admin.site.register(Regional)
admin.site.register(EventType)
admin.site.register(Presence)
admin.site.register(Event)