# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20171122_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
