# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0014_auto_20161018_0958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apprequest',
            old_name='contact',
            new_name='name',
        ),
    ]
