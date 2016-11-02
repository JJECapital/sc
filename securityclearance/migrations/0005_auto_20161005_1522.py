# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0004_auto_20161005_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='sc',
            field=multiselectfield.db.fields.MultiSelectField(default=b'None', max_length=17, choices=[(1, b'Developed Vetting (DV)'), (2, b'Security Check (SC)'), (3, b'Baseline Personnel Security Standard (BPSS)'), (4, b'Counter Terrorist Check (CTC)'), (5, b'NATO Cleared (NR/NC/NS/CTS)'), (6, b'Metropolitan Police Service (MPS:IVC/MV)'), (7, b'Security Industry Authority (SIA)'), (8, b'[Enhanced] Disclosure and Barring Services (DBS/EDBS)'), (9, b'None')]),
        ),
    ]
