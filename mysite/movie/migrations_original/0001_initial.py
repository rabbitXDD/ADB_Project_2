# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
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
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('birthday', models.DateField()),
                ('phoneNumber', models.CharField(blank=True, max_length=200, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
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
                ('combo', models.ForeignKey(blank=True, to='movie.Combo', null=True)),
                ('meal', models.ForeignKey(blank=True, to='movie.Meal', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=1)),
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
                ('showtime', models.DateTimeField()),
                ('price', models.IntegerField(default=200)),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
            options={
                'db_table': 'showtimes',
            },
        ),
        migrations.AddField(
            model_name='seat',
            name='showtimes',
            field=models.ForeignKey(to='movie.Showtimes'),
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
    ]
