# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('platalbank_core', '0004_auto_20151120_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='account', default=1),
        ),
    ]
