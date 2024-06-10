# Generated by Django 4.0.6 on 2024-04-06 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('ano', models.IntegerField(blank=True, null=True)),
                ('duracao', models.CharField(default='???', max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='album',
            old_name='ano',
            new_name='ano_lancamento',
        ),
        migrations.RenameField(
            model_name='banda',
            old_name='idade',
            new_name='ano_criacao',
        ),
        migrations.RemoveField(
            model_name='album',
            name='capa',
        ),
        migrations.RemoveField(
            model_name='banda',
            name='foto',
        ),
        migrations.AddField(
            model_name='album',
            name='titulo',
            field=models.CharField(default='Album sem nome', max_length=100),
        ),
        migrations.AddField(
            model_name='banda',
            name='nacionalidade',
            field=models.CharField(default='Desconhecido', max_length=100),
        ),
        migrations.DeleteModel(
            name='Musica',
        ),
        migrations.AddField(
            model_name='musicas',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandas.album'),
        ),
    ]
