# Generated by Django 4.0.4 on 2022-04-18 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoas_cad',
            name='foto_pessoa',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
