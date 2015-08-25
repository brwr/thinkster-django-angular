# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translocatome', '0002_auto_20150820_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='EffectValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.SmallIntegerField(choices=[(0, b'float'), (1, b'unknown'), (2, b'both')])),
                ('value', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='effect_all',
            field=models.ForeignKey(related_name='effect_all', to='translocatome.EffectValue'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='interaction',
            name='effect_final',
            field=models.ForeignKey(related_name='effect_final', to='translocatome.EffectValue'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='interaction',
            name='interaction_type',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='interaction',
            name='score',
            field=models.SmallIntegerField(),
            preserve_default=True,
        ),
    ]
