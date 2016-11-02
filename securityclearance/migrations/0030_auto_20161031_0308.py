# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0029_auto_20161028_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apprequest',
            name='comments',
            field=models.TextField(default=b'', max_length=256, null=True, blank=True),
        ),
    ]
