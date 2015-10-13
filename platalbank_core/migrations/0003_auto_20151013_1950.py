# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('platalbank_core', '0002_auto_20151010_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.BigIntegerField(),
        ),
    ]
