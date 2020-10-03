# Generated by Django 3.1 on 2020-08-12 15:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2020, 8, 12, 21, 3, 14, 730874))),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FilterHeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2020, 8, 12, 21, 3, 14, 730374))),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FilterLength',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2020, 8, 12, 21, 3, 14, 728874))),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FilterVolume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2020, 8, 12, 21, 3, 14, 731374))),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FilterWidth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2020, 8, 12, 21, 3, 14, 729872))),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuboid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2020, 8, 12, 21, 3, 14, 726872))),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_api.filterarea')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('height', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_api.filterheight')),
                ('length', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_api.filterlength')),
                ('volume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_api.filtervolume')),
                ('width', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_api.filterwidth')),
            ],
        ),
    ]