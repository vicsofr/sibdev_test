# Generated by Django 4.1.7 on 2023-02-22 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=30)),
                ('item', models.CharField(max_length=50)),
                ('total', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Deal',
                'verbose_name_plural': 'Deals',
                'db_table': 'deals',
            },
        ),
    ]