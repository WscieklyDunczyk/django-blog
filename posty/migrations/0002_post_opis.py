# Generated by Django 4.0.1 on 2022-02-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='opis',
            field=models.TextField(default='qwe'),
        ),
    ]
