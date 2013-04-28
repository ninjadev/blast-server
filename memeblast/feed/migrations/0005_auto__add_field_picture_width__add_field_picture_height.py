# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Picture.width'
        db.add_column(u'feed_picture', 'width',
                      self.gf('django.db.models.fields.IntegerField')(default=1024),
                      keep_default=False)

        # Adding field 'Picture.height'
        db.add_column(u'feed_picture', 'height',
                      self.gf('django.db.models.fields.IntegerField')(default=1024),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Picture.width'
        db.delete_column(u'feed_picture', 'width')

        # Deleting field 'Picture.height'
        db.delete_column(u'feed_picture', 'height')


    models = {
        u'feed.picture': {
            'Meta': {'object_name': 'Picture'},
            'height': ('django.db.models.fields.IntegerField', [], {'default': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture_url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '1024'})
        }
    }

    complete_apps = ['feed']