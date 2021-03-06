# Generated by Django 3.1 on 2020-08-13 13:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crud_api', '0007_auto_20200813_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuboid',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crud_api.filterarea'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cuboid',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cuboid',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 13, 32, 3, 154477)),
        ),
        migrations.AlterField(
            model_name='cuboid',
            name='height',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_api.filterheight'),
        ),
        migrations.AlterField(
            model_name='cuboid',
            name='volume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_api.filtervolume'),
        ),
        migrations.AlterField(
            model_name='cuboid',
            name='width',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_api.filterwidth'),
        ),
        migrations.AlterField(
            model_name='filterarea',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 13, 32, 3, 156827)),
        ),
        migrations.AlterField(
            model_name='filterheight',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 13, 32, 3, 156340)),
        ),
        migrations.AlterField(
            model_name='filterlength',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 13, 32, 3, 155306)),
        ),
        migrations.AlterField(
            model_name='filtervolume',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 13, 32, 3, 157269)),
        ),
        migrations.AlterField(
            model_name='filterwidth',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 13, 32, 3, 155767)),
        ),
    ]
