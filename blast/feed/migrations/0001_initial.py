# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture_url', models.CharField(max_length=100)),
                ('posted_on', models.DateTimeField()),
                ('text', models.CharField(max_length=20, null=True, blank=True)),
                ('published', models.BooleanField(default=False)),
                ('width', models.IntegerField(default=1024)),
                ('height', models.IntegerField(default=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
