# Generated by Django 4.0.3 on 2022-07-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiel', '0004_alter_materiel_etat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiel',
            name='Etat',
            field=models.TextField(choices=[('Aucun', 'Aucun'), ('Très bon', 'Très bon'), ('bon', 'Bon'), ('Moyen', 'Moyen'), ('Mauvais', 'Mauvais'), ('En panne', 'En panne')], default='Aucun', max_length=200),
        ),
    ]
