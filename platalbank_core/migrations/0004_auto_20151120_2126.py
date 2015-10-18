# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('platalbank_core', '0003_auto_20151013_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 11, 20, 21, 26, 20, 408298, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 11, 20, 21, 26, 34, 22220, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
