# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_seatsorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderMeal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meal', models.ForeignKey(to='movie.Meal')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='meal',
        ),
        migrations.AddField(
            model_name='ordermeal',
            name='order',
            field=models.ForeignKey(to='movie.Order'),
        ),
    ]
