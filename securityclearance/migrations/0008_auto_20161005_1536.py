# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0007_auto_20161005_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='BPSS',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='CTC',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='DBS',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='DV',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='MPS',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='NATO',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='SC',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='SIA',
            field=models.BooleanField(),
        ),
    ]
