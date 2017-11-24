# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_seat_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtimes',
            name='showtime',
            field=models.DateTimeField(),
        ),
    ]
