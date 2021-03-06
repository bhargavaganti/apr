# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0004_auto_20150607_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='custom_reminder',
            field=models.BooleanField(default=False, help_text='If you check this, we will use the custom script provided by you below.  Leave it blank to use the system default.', verbose_name='Use custom script'),
        ),
    ]
