# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0023_apprequest_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apprequest',
            name='attachment',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
