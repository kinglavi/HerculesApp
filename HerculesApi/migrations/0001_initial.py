# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('goal', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(default=None)),
                ('description', models.CharField(max_length=500)),
                ('gift_discount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('punch_counter', models.IntegerField(default=0)),
                ('campaign', models.OneToOneField(to='HerculesApi.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gifts', models.ManyToManyField(to='HerculesApi.Campaign', null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500, blank=True)),
                ('sticker_counter', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=500)),
                ('is_used', models.BooleanField(default=False)),
                ('product', models.ForeignKey(to='HerculesApi.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(max_length=30)),
                ('company', models.ForeignKey(to='HerculesApi.Company')),
                ('managers', models.ManyToManyField(default=None, to='auth.Group')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(to='HerculesApi.Store'),
        ),
        migrations.AddField(
            model_name='company',
            name='managers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='card',
            name='owner',
            field=models.ForeignKey(to='HerculesApi.Customer'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='products',
            field=models.ManyToManyField(to='HerculesApi.Product'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='store',
            field=models.ForeignKey(to='HerculesApi.Store'),
        ),
    ]
