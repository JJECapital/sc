# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0030_auto_20161031_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='apprequest',
            name='reference',
            field=models.CharField(default='TEST0001', max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apprequest',
            name='comments',
            field=models.CharField(default=b'', max_length=256, null=True, blank=True),
        ),
    ]
