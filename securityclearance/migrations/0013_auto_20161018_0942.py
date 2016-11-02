# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0012_apprequest_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='apprequest',
            name='status',
            field=models.CharField(default=b'Submitted', max_length=8, choices=[(b'Submitted', b'Submitted'), (b'Packaging', b'Packaging'), (b'UAT', b'In UAT'), (b'Completed', b'Completed')]),
        ),
        migrations.AlterField(
            model_name='apprequest',
            name='priority',
            field=models.CharField(default=b'Low', max_length=8, choices=[(b'High', b'High'), (b'Medium', b'Medium'), (b'Low', b'Low')]),
        ),
    ]
