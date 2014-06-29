# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Yokoshi.indication'
        db.delete_column(u'registration_yokoshi', 'indication_id')

        # Adding M2M table for field indication on 'Yokoshi'
        m2m_table_name = db.shorten_name(u'registration_yokoshi_indication')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_yokoshi', models.ForeignKey(orm[u'registration.yokoshi'], null=False)),
            ('to_yokoshi', models.ForeignKey(orm[u'registration.yokoshi'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_yokoshi_id', 'to_yokoshi_id'])


    def backwards(self, orm):
        # Adding field 'Yokoshi.indication'
        db.add_column(u'registration_yokoshi', 'indication',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.Yokoshi'], unique=True, null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field indication on 'Yokoshi'
        db.delete_table(db.shorten_name(u'registration_yokoshi_indication'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'registration.address': {
            'Meta': {'unique_together': "(('street_name', 'house_number', 'neighborhood'),)", 'object_name': 'Address'},
            'additional_information': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'house_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'neighborhood': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Neighborhood']", 'null': 'True', 'blank': 'True'}),
            'street_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'})
        },
        u'registration.city': {
            'Meta': {'unique_together': "(('name', 'state'),)", 'object_name': 'City'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.State']"})
        },
        u'registration.country': {
            'Meta': {'object_name': 'Country'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        u'registration.event': {
            'Meta': {'unique_together': "(('event_type', 'begin_date_time'),)", 'object_name': 'Event'},
            'begin_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'}),
            'event_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.EventType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'registration.eventtype': {
            'Meta': {'object_name': 'EventType'},
            'additional_information': ('django.db.models.fields.TextField', [], {'max_length': '30000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        u'registration.han': {
            'Meta': {'object_name': 'Han'},
            'additional_information': ('django.db.models.fields.TextField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'regional': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Regional']"})
        },
        u'registration.neighborhood': {
            'Meta': {'unique_together': "(('name', 'city'),)", 'object_name': 'Neighborhood'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.City']", 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'registration.presence': {
            'Meta': {'object_name': 'Presence'},
            'additional_information': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'begin_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_first_time': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yokoshi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Yokoshi']"})
        },
        u'registration.regional': {
            'Meta': {'object_name': 'Regional'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'parent_regional': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['registration.Regional']", 'null': 'True', 'blank': 'True'})
        },
        u'registration.state': {
            'Meta': {'unique_together': "(('name', 'country'),)", 'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Country']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        u'registration.yokoshi': {
            'Meta': {'object_name': 'Yokoshi'},
            'additional_information': ('django.db.models.fields.TextField', [], {'max_length': '30000', 'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Address']", 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'complete_name': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_index': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'han': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Han']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indication': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['registration.Yokoshi']", 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'is_inactive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_mikumite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_mtai': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_ossuewanin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'omitama_level': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'phonetic_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'seminary_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['registration']