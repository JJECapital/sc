# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import securityclearance.models


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0024_auto_20161021_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apprequest',
            name='attachment',
            field=models.FileField(null=True, upload_to=securityclearance.models.upload_location, blank=True),
        ),
    ]
