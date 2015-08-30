# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translocatome', '0007_auto_20150822_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metadata',
            name='interaction',
        ),
        migrations.AddField(
            model_name='interaction',
            name='meta_data',
            field=models.ForeignKey(default=None, to='translocatome.MetaData'),
            preserve_default=False,
        ),
    ]
