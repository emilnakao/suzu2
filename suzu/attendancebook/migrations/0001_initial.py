# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-11 22:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('street_name', models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='Address|street_name')),
                ('house_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Address|house_number')),
                ('zip_code', models.IntegerField(blank=True, max_length=12, null=True, verbose_name='Address|zip_code')),
                ('additional_information', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Address|additional_information')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='City|name')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Country|name')),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date_time', models.DateTimeField(verbose_name='Event|begin_date_time')),
                ('details', models.CharField(blank=True, max_length=20000, null=True, verbose_name='Event|details')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='EventType|name')),
                ('additional_information', models.TextField(blank=True, max_length=30000, null=True, verbose_name='EventType|additional_information')),
            ],
            options={
                'verbose_name': 'event_type',
                'verbose_name_plural': 'event_types',
            },
        ),
        migrations.CreateModel(
            name='Han',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(blank=True, db_index=True, max_length=100, null=True, unique=True, verbose_name='Han|name')),
                ('additional_information', models.TextField(blank=True, max_length=20000, null=True, verbose_name='Han|additional_information')),
            ],
            options={
                'verbose_name': 'han',
                'verbose_name_plural': 'hans',
            },
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Neighborhood|name')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.City', verbose_name='Neighborhood|city')),
            ],
            options={
                'verbose_name': 'neighborhood',
                'verbose_name_plural': 'neighborhoods',
            },
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date_time', models.DateTimeField(null=True, verbose_name='Presence|begin_date_time')),
                ('additional_information', models.TextField(max_length=2000, verbose_name='Presence|additional_information')),
                ('is_first_time', models.BooleanField(default=False, verbose_name='Presence|is_first_time')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendancebook.Event', verbose_name='Presence|event')),
            ],
            options={
                'verbose_name': 'presence',
                'verbose_name_plural': 'presences',
            },
        ),
        migrations.CreateModel(
            name='Regional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Regional|name')),
                ('parent_regional', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.Regional', verbose_name='Regional|parent_regional')),
            ],
            options={
                'verbose_name': 'regional',
                'verbose_name_plural': 'regionals',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='State|name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendancebook.Country', verbose_name='State|country')),
            ],
            options={
                'verbose_name': 'state',
                'verbose_name_plural': 'states',
            },
        ),
        migrations.CreateModel(
            name='Yokoshi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('complete_name', models.CharField(db_index=True, max_length=500, verbose_name='Yokoshi|complete_name')),
                ('phonetic_name', models.CharField(blank=True, db_index=True, editable=False, max_length=500, null=True, verbose_name='Yokoshi|phonetic_name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Yokoshi|email')),
                ('phone', models.CharField(blank=True, max_length=40, null=True, verbose_name='Yokoshi|phone')),
                ('additional_information', models.TextField(blank=True, max_length=30000, null=True, verbose_name='Yokoshi|additional_information')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Yokoshi|birthday')),
                ('is_inactive', models.BooleanField(default=False, verbose_name='Yokoshi|is_inactive')),
                ('seminary_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Yokoshi|seminary_number')),
                ('is_mtai', models.BooleanField(default=False, verbose_name='Yokoshi|is_mtai')),
                ('is_ossuewanin', models.BooleanField(default=False, verbose_name='Yokoshi|is_ossuewanin')),
                ('is_mikumite', models.BooleanField(default=False, verbose_name='Yokoshi|is_mikumite')),
                ('omitama_level', models.CharField(choices=[('none', 'none_omitama_level'), ('basic', 'basic_omitama_level'), ('intermediate', 'intermediate_omitama_level'), ('advanced', 'advanced_omitama_level')], default='none', max_length=50)),
                ('last_registration_update', models.DateField(blank=True, null=True, verbose_name='Yokoshi|last_registration_update')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.Address', verbose_name='Yokoshi|address')),
                ('han', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.Han', verbose_name='Yokoshi|han')),
                ('indication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.Yokoshi', verbose_name='Yokoshi|indication')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yokoshi|user')),
            ],
            options={
                'verbose_name': 'yokoshi',
                'verbose_name_plural': 'yokoshis',
            },
        ),
        migrations.AddField(
            model_name='presence',
            name='yokoshi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendancebook.Yokoshi', verbose_name='Presence|yokoshi'),
        ),
        migrations.AddField(
            model_name='han',
            name='regional',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.Regional', verbose_name='Han|regional'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendancebook.EventType', verbose_name='Event|event_type'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendancebook.State', verbose_name='City|state'),
        ),
        migrations.AddField(
            model_name='address',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendancebook.Neighborhood', verbose_name='Address|neighborhood'),
        ),
        migrations.AlterUniqueTogether(
            name='state',
            unique_together=set([('name', 'country')]),
        ),
        migrations.AlterUniqueTogether(
            name='neighborhood',
            unique_together=set([('name', 'city')]),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('event_type', 'begin_date_time')]),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('name', 'state')]),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([('street_name', 'house_number', 'neighborhood')]),
        ),
    ]
