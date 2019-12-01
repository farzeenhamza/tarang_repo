# Generated by Django 2.2 on 2019-11-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191129_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='college',
            field=models.CharField(default='gcek', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile_number',
            field=models.CharField(default=77, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='place',
            field=models.CharField(default='clt', max_length=30),
            preserve_default=False,
        ),
    ]