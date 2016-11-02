# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(default=b'<undisclosed>', max_length=64),
        ),
        migrations.AddField(
            model_name='job',
            name='sc',
            field=models.CharField(default=b'None', max_length=8, choices=[(b'DV', b'Developed Vetting (DV)'), (b'SC', b'Security Check (SC)'), (b'BPSS', b'Baseline Personnel Security Standard (BPSS)'), (b'CTC', b'Counter Terrorist Check (CTC)'), (b'NATO', b'NATO Cleared (NR/NC/NS/CTS)'), (b'MPS', b'Metropolitan Police Service (MPS:IVC/MV)'), (b'SIA', b'Security Industry Authority (SIA)'), (b'DBS/EDBS', b'[Enhanced] Disclosure and Barring Services (DBS/EDBS)'), (b'None', b'None')]),
        ),
        migrations.AddField(
            model_name='job',
            name='url',
            field=models.URLField(default=b'<no url>'),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
