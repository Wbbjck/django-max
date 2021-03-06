# Generated by Django 4.0.1 on 2022-01-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Protocols',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.PositiveIntegerField(default=1, null=True, verbose_name='Номер протокола')),
                ('date', models.DateField(verbose_name='Дата')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес дома')),
                ('file', models.FileField(upload_to='protocols/%Y/')),
            ],
        ),
    ]
