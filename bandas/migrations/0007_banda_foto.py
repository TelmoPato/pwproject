# Generated by Django 4.0.6 on 2024-06-01 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0006_remove_album_imagem_url_album_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='foto',
            field=models.ImageField(default='bandas/default.jpg', upload_to='bandas/'),
        ),
    ]
