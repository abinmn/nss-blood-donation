# Generated by Django 3.0.3 on 2020-02-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='height',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
