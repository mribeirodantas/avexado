# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('name', models.CharField(max_length=b'20', serialize=False, primary_key=True)),
                ('content', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
