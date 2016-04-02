# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platalbank_core', '0006_frankizuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frankizuser',
            name='phone',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
