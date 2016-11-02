# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0002_auto_20161004_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=128)),
                ('phone', models.CharField(max_length=16)),
                ('sc', multiselectfield.db.fields.MultiSelectField(max_length=41, choices=[(b'DV', b'Developed Vetting (DV)'), (b'SC', b'Security Check (SC)'), (b'BPSS', b'Baseline Personnel Security Standard (BPSS)'), (b'CTC', b'Counter Terrorist Check (CTC)'), (b'NATO', b'NATO Cleared (NR/NC/NS/CTS)'), (b'MPS', b'Metropolitan Police Service (MPS:IVC/MV)'), (b'SIA', b'Security Industry Authority (SIA)'), (b'DBS/EDBS', b'[Enhanced] Disclosure and Barring Services (DBS/EDBS)'), (b'None', b'None')])),
            ],
        ),
    ]
