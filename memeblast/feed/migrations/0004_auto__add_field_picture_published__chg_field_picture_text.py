# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Picture.published'
        db.add_column(u'feed_picture', 'published',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Picture.text'
        db.alter_column(u'feed_picture', 'text', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

    def backwards(self, orm):
        # Deleting field 'Picture.published'
        db.delete_column(u'feed_picture', 'published')


        # Changing field 'Picture.text'
        db.alter_column(u'feed_picture', 'text', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))

    models = {
        u'feed.picture': {
            'Meta': {'object_name': 'Picture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture_url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['feed']