# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0003_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='sc',
            field=multiselectfield.db.fields.MultiSelectField(default=b'None', max_length=41, choices=[(b'DV', b'Developed Vetting (DV)'), (b'SC', b'Security Check (SC)'), (b'BPSS', b'Baseline Personnel Security Standard (BPSS)'), (b'CTC', b'Counter Terrorist Check (CTC)'), (b'NATO', b'NATO Cleared (NR/NC/NS/CTS)'), (b'MPS', b'Metropolitan Police Service (MPS:IVC/MV)'), (b'SIA', b'Security Industry Authority (SIA)'), (b'DBS/EDBS', b'[Enhanced] Disclosure and Barring Services (DBS/EDBS)'), (b'None', b'None')]),
        ),
    ]
