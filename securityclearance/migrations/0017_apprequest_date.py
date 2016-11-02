# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0016_auto_20161018_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='apprequest',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 10, 19, 8, 23, 3, 727214, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
