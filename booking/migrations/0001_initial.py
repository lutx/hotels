# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('booked_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=100)),
                ('guest', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_code', django_countries.fields.CountryField(max_length=2)),
                ('star_rating', models.DecimalField(max_digits=3, decimal_places=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'")])),
                ('address', models.CharField(max_length=100)),
                ('avatar', models.ImageField(upload_to=b'media/avatars', blank=True)),
                ('city', models.CharField(max_length=50)),
                ('url', models.URLField(validators=[django.core.validators.URLValidator])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hotel_Chain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chain_name', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'media/images')),
                ('hotel', models.ForeignKey(to='booking.Hotel', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=500)),
                ('receiver', models.ForeignKey(related_name='receiver', blank=True, to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sender', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('booking', models.ForeignKey(to='booking.Booking')),
                ('guest', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('hotel', models.ForeignKey(to='booking.Hotel', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('avatar', models.ImageField(upload_to=b'media/images', blank=True)),
                ('description', models.CharField(max_length=400)),
                ('hotel', models.ForeignKey(to='booking.Hotel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_type', models.CharField(max_length=10, choices=[(b'single', b'Single'), (b'double', b'Double'), (b'twin', b'Twin'), (b'triple', b'Triple'), (b'multiple', b'Multiple')])),
                ('room_standard', models.CharField(max_length=100)),
                ('smoking_in', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(to='booking.Room_Type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='room',
            field=models.ForeignKey(to='booking.Room', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_chain',
            field=models.ForeignKey(blank=True, to='booking.Hotel_Chain', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hotel',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.ForeignKey(to='booking.Rating', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='room',
            field=models.ForeignKey(to='booking.Room', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(to='booking.Hotel', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(to='booking.Room', blank=True),
            preserve_default=True,
        ),
    ]
