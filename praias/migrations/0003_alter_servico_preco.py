# Generated by Django 4.0.6 on 2024-04-23 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praias', '0002_praia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='preco',
            field=models.CharField(max_length=50),
        ),
    ]
