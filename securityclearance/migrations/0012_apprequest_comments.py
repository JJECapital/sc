# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0011_auto_20161018_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='apprequest',
            name='comments',
            field=models.CharField(default=b'', max_length=256),
        ),
    ]
