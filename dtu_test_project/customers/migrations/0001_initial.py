# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tenant_schemas.postgresql_backend.base


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('domain_url', models.CharField(max_length=128, unique=True)),
                ('schema_name', models.CharField(max_length=63, unique=True, validators=[tenant_schemas.postgresql_backend.base._check_schema_name])),
                ('slug', models.SlugField(verbose_name='Tenant URL Name', blank=True)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
