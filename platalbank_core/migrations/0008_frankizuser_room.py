# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platalbank_core', '0007_auto_20160402_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='frankizuser',
            name='room',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
