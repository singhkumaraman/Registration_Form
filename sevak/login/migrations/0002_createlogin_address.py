# Generated by Django 4.0.6 on 2022-07-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createlogin',
            name='address',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]