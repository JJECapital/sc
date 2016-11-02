# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0028_auto_20161024_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apprequest',
            old_name='packagetype',
            new_name='package_type',
        ),
    ]
