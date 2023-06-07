# Generated by Django 4.2.2 on 2023-06-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='fees_in_world',
            field=models.PositiveIntegerField(default=0, help_text='Указывать сумму в долларах', verbose_name='Сборы в мире'),
        ),
    ]
