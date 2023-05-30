# Generated by Django 4.2.1 on 2023-05-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ferramentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('ativa', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'BD Ferramentas Cadastradas',
                'verbose_name_plural': 'BD Ferramentas Cadastradas',
                'db_table': 'db_ferramentas_cadastradas',
            },
        ),
    ]
