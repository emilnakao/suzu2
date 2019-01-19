# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext


class AttendancebookConfig(AppConfig):
    name = 'attendancebook'
    verbose_name = ugettext('attendancebook.verbose_name')
