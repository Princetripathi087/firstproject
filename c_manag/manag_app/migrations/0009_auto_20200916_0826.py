# Generated by Django 3.0.7 on 2020-09-16 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manag_app', '0008_requarement_lorrytype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requarement',
            name='drivName',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
