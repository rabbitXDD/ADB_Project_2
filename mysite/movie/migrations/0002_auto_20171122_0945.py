# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(serialize=False, primary_key=True)),
                ('account', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=20)),
                ('customer_name', models.CharField(max_length=25)),
                ('birthday', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=20)),
                ('vip', models.CharField(max_length=10, db_column='VIP')),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Combo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'combo',
            },
        ),
        migrations.CreateModel(
            name='Combo_Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('combo', models.ForeignKey(to='movie.Combo')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('kind', models.CharField(default=2, max_length=10, choices=[(1, 'Beverage'), (2, 'Food')])),
                ('flavor', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'meal',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('type', models.CharField(max_length=20)),
                ('runtime', models.CharField(max_length=20)),
                ('director', models.CharField(max_length=25)),
                ('actor', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=b'')),
            ],
            options={
                'db_table': 'movie',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, choices=[(1, 'Unconfirmed'), (2, 'Confirmed'), (3, 'Canceled')])),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'seat',
            },
        ),
        migrations.CreateModel(
            name='Showtimes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cinema', models.CharField(max_length=10)),
                ('showtime', models.TimeField()),
                ('price', models.IntegerField(default=200)),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
            options={
                'db_table': 'showtimes',
            },
        ),
        migrations.CreateModel(
            name='ComboOrder',
            fields=[
                ('order_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='movie.Order')),
            ],
            bases=('movie.order',),
        ),
        migrations.CreateModel(
            name='NormalOrder',
            fields=[
                ('order_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='movie.Order')),
                ('meal', models.ForeignKey(to='movie.Meal')),
            ],
            bases=('movie.order',),
        ),
        migrations.AddField(
            model_name='seat',
            name='showtimes',
            field=models.ForeignKey(to='movie.Showtimes'),
        ),
        migrations.AddField(
            model_name='order',
            name='seat',
            field=models.ForeignKey(to='movie.Seat'),
        ),
        migrations.AddField(
            model_name='order',
            name='showtimes',
            field=models.ForeignKey(to='movie.Showtimes'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='combo_meal',
            name='meal',
            field=models.ForeignKey(to='movie.Meal'),
        ),
        migrations.AddField(
            model_name='combo',
            name='movie',
            field=models.ForeignKey(to='movie.Movie'),
        ),
        migrations.AddField(
            model_name='comboorder',
            name='comboOrder',
            field=models.ForeignKey(to='movie.Combo'),
        ),
    ]
