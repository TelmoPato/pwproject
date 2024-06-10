# Generated by Django 4.0.6 on 2024-06-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0008_remove_banda_foto_banda_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banda',
            name='imagem',
        ),
        migrations.AddField(
            model_name='banda',
            name='foto',
            field=models.ImageField(default='bandas/default.jpg', upload_to='bandas/'),
        ),
    ]
