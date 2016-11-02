# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0008_auto_20161005_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=128)),
                ('phone', models.CharField(max_length=16)),
                ('vendor', models.CharField(max_length=64)),
                ('app', models.CharField(max_length=64)),
                ('version', models.CharField(max_length=16)),
                ('os', models.CharField(default=b'Win10', max_length=16, choices=[(b'Win10', b'Windows 10'), (b'Win81', b'Windows 8.1'), (b'Win7', b'Windows 7'), (b'WinXP', b'Windows XP')])),
                ('packagetype', models.CharField(default=b'MSI', max_length=16, choices=[(b'MSI', b'MSI'), (b'AppV46', b'App-V 4.6'), (b'AppV50', b'App-V 5.0')])),
                ('complexity', models.CharField(default=b'M', max_length=8, choices=[(b'S', b'Simple'), (b'M', b'Medium'), (b'C', b'Complex')])),
            ],
        ),
    ]
