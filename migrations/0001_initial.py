# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='XMLSitemap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('change_frequency', models.CharField(default=b'weekly', max_length=20, choices=[(b'always', 'Always'), (b'hourly', 'hourly'), (b'daily', 'daily'), (b'weekly', 'weekly'), (b'monthly', 'monthly'), (b'yearly', 'yearly'), (b'never', 'never')])),
            ],
            options={
                'verbose_name': 'Xml Sitemap',
                'verbose_name_plural': 'Xml Sitemaps',
            },
            bases=(models.Model,),
        ),
    ]
