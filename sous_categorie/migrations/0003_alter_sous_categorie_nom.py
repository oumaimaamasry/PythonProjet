# Generated by Django 4.0.3 on 2022-08-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sous_categorie', '0002_remove_sous_categorie_categorie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sous_categorie',
            name='Nom',
            field=models.TextField(max_length=30, null=True),
        ),
    ]
