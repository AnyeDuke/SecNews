# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sec_News', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newssql',
            name='Art_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
