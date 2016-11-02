# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0022_auto_20161020_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='apprequest',
            name='attachment',
            field=models.FileField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]
