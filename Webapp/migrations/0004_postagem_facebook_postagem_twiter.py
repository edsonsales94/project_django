# Generated by Django 4.0.4 on 2022-05-05 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0003_alter_postagem_autor_alter_postagem_publicar'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagem',
            name='facebook',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postagem',
            name='twiter',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]
