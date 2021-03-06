# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import django.utils.timezone
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='username', unique=True, max_length=30, error_messages={'unique': 'A user with that username already exists.'}, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('room', models.CharField(max_length=10, null=True)),
                ('promo', models.CharField(max_length=128, null=True)),
                ('groups', models.ManyToManyField(related_name='user_set', verbose_name='groups', to='auth.Group', related_query_name='user', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', verbose_name='user permissions', to='auth.Permission', related_query_name='user', blank=True, help_text='Specific permissions for this user.')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('balance', models.BigIntegerField(default=0)),
                ('description', models.CharField(max_length=1024)),
                ('short_name', models.CharField(max_length=128, unique=True)),
                ('owner', models.ForeignKey(related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('label', models.CharField(max_length=1024)),
                ('through_khube', models.BooleanField()),
                ('writable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FrankizUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('hruid', models.CharField(max_length=256)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('room', models.CharField(max_length=10, null=True)),
                ('promo', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('state', models.CharField(max_length=1, default='P', choices=[('P', 'PENDING'), ('A', 'AUTHORIZED'), ('R', 'REJECTED'), ('X', 'ABORTED'), ('C', 'COMPLETED')])),
                ('amount', models.BigIntegerField()),
                ('label', models.CharField(max_length=1024)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('credited_account', models.ForeignKey(related_name='in_transactions', to='platalbank_core.Account')),
                ('debited_account', models.ForeignKey(related_name='out_transactions', to='platalbank_core.Account')),
                ('event', models.ForeignKey(to='platalbank_core.Event')),
            ],
        ),
    ]
