# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='last_edited_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 0, 50, 23, 921066, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
