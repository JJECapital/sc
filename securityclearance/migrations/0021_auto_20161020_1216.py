# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0020_apprequest_assigned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apprequest',
            name='assigned',
            field=models.CharField(default=b'Not Assigned', max_length=64, choices=[(b'Not Assigned', b'Not Assigned'), (b'Assigned', b'Assigned')]),
        ),
    ]
