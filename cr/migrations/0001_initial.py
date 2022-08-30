# Generated by Django 4.1 on 2022-08-30 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='ФИО')),
                ('address', models.CharField(blank=True, max_length=60, null=True, verbose_name='Адрес')),
                ('phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]