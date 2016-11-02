# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0005_auto_20161005_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='sc',
        ),
        migrations.AddField(
            model_name='candidate',
            name='dv',
            field=models.BooleanField(default=b'FALSE'),
        ),
    ]
