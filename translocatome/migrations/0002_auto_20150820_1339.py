# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translocatome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='gene_name',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='GeneName',
        ),
        migrations.AlterField(
            model_name='node',
            name='uni_prot_ac',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='UniProtAc',
        ),
    ]
