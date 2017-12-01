# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20171125_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='combo',
            name='name',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]
