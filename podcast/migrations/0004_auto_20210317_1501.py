# Generated by Django 3.1.7 on 2021-03-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0003_auto_20210317_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='audio',
        ),
        migrations.AddField(
            model_name='episode',
            name='podcast',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]