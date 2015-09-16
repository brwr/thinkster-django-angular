# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translocatome', '0013_auto_20150916_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='interaction_type',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
