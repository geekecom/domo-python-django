# Generated by Django 2.2.20 on 2021-04-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='control',
            name='name',
            field=models.CharField(default='control', max_length=20),
            preserve_default=False,
        ),
    ]
