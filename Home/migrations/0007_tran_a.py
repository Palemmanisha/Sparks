# Generated by Django 3.0.8 on 2020-09-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20200916_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='tran',
            name='a',
            field=models.BooleanField(default=False),
        ),
    ]
