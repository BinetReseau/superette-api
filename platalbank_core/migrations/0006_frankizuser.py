# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platalbank_core', '0005_account_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrankizUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hruid', models.CharField(max_length=256)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
    ]
