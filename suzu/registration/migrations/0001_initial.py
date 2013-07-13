# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Regional'
        db.create_table(u'registration_regional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100, db_index=True)),
            ('parent_regional', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['registration.Regional'], null=True, blank=True)),
        ))
        db.send_create_signal(u'registration', ['Regional'])

        # Adding model 'Han'
        db.create_table(u'registration_han', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, unique=True, null=True, blank=True)),
            ('regional', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Regional'])),
            ('additional_information', self.gf('django.db.models.fields.TextField')(max_length=20000, null=True, blank=True)),
        ))
        db.send_create_signal(u'registration', ['Han'])

        # Adding model 'Yokoshi'
        db.create_table(u'registration_yokoshi', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('complete_name', self.gf('django.db.models.fields.CharField')(max_length=500, db_index=True)),
            ('phonetic_name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=500, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Address'], null=True, blank=True)),
            ('additional_information', self.gf('django.db.models.fields.TextField')(max_length=30000, null=True, blank=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True)),
            ('is_inactive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('seminary_number', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('han', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Han'], null=True, blank=True)),
            ('is_mtai', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_ossuewanin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_mikumite', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('omitama_level', self.gf('django.db.models.fields.CharField')(default='none', max_length=50)),
        ))
        db.send_create_signal(u'registration', ['Yokoshi'])

        # Adding model 'Country'
        db.create_table(u'registration_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100, db_index=True)),
        ))
        db.send_create_signal(u'registration', ['Country'])

        # Adding model 'State'
        db.create_table(u'registration_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100, db_index=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Country'])),
        ))
        db.send_create_signal(u'registration', ['State'])

        # Adding unique constraint on 'State', fields ['name', 'country']
        db.create_unique(u'registration_state', ['name', 'country_id'])

        # Adding model 'City'
        db.create_table(u'registration_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100, db_index=True)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.State'])),
        ))
        db.send_create_signal(u'registration', ['City'])

        # Adding unique constraint on 'City', fields ['name', 'state']
        db.create_unique(u'registration_city', ['name', 'state_id'])

        # Adding model 'Neighborhood'
        db.create_table(u'registration_neighborhood', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.City'], null=True, blank=True)),
        ))
        db.send_create_signal(u'registration', ['Neighborhood'])

        # Adding unique constraint on 'Neighborhood', fields ['name', 'city']
        db.create_unique(u'registration_neighborhood', ['name', 'city_id'])

        # Adding model 'Address'
        db.create_table(u'registration_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('street_name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=500, null=True, blank=True)),
            ('house_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.IntegerField')(max_length=12, null=True, blank=True)),
            ('neighborhood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Neighborhood'], null=True, blank=True)),
            ('additional_information', self.gf('django.db.models.fields.TextField')(max_length=2000, null=True, blank=True)),
        ))
        db.send_create_signal(u'registration', ['Address'])

        # Adding unique constraint on 'Address', fields ['street_name', 'house_number', 'neighborhood']
        db.create_unique(u'registration_address', ['street_name', 'house_number', 'neighborhood_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Address', fields ['street_name', 'house_number', 'neighborhood']
        db.delete_unique(u'registration_address', ['street_name', 'house_number', 'neighborhood_id'])

        # Removing unique constraint on 'Neighborhood', fields ['name', 'city']
        db.delete_unique(u'registration_neighborhood', ['name', 'city_id'])

        # Removing unique constraint on 'City', fields ['name', 'state']
        db.delete_unique(u'registration_city', ['name', 'state_id'])

        # Removing unique constraint on 'State', fields ['name', 'country']
        db.delete_unique(u'registration_state', ['name', 'country_id'])

        # Deleting model 'Regional'
        db.delete_table(u'registration_regional')

        # Deleting model 'Han'
        db.delete_table(u'registration_han')

        # Deleting model 'Yokoshi'
        db.delete_table(u'registration_yokoshi')

        # Deleting model 'Country'
        db.delete_table(u'registration_country')

        # Deleting model 'State'
        db.delete_table(u'registration_state')

        # Deleting model 'City'
        db.delete_table(u'registration_city')

        # Deleting model 'Neighborhood'
        db.delete_table(u'registration_neighborhood')

        # Deleting model 'Address'
        db.delete_table(u'registration_address')


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
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'complete_name': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_index': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'han': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Han']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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