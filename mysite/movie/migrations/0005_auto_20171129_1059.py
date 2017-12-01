# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_combo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combo',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
