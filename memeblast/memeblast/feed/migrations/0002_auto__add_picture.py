# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Picture'
        db.create_table(u'feed_picture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('picture_url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('posted_on', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'feed', ['Picture'])


    def backwards(self, orm):
        # Deleting model 'Picture'
        db.delete_table(u'feed_picture')


    models = {
        u'feed.picture': {
            'Meta': {'object_name': 'Picture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture_url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['feed']