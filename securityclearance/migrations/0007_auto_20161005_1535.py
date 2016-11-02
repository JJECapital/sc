# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0006_auto_20161005_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='dv',
            new_name='DV',
        ),
        migrations.AddField(
            model_name='candidate',
            name='BPSS',
            field=models.BooleanField(default=b'FALSE'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='CTC',
            field=models.BooleanField(default=b'FALSE'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='DBS',
            field=models.BooleanField(default=b'FALSE'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='MPS',
            field=models.BooleanField(default=b'FALSE'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='NATO',
            field=models.BooleanField(default=b'FALSE'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='SC',
            field=models.BooleanField(default=b'FALSE'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='SIA',
            field=models.BooleanField(default=b'FALSE'),
        ),
    ]
