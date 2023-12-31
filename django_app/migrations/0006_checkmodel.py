# Generated by Django 4.2.1 on 2023-07-09 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0005_datemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('state', models.CharField(choices=[('kerala', 'kerala'), ('tamilnadu', 'tamilnadu'), ('karnataka', 'karnataka')], max_length=20)),
                ('eng', models.BooleanField()),
                ('mal', models.BooleanField()),
                ('hind', models.BooleanField()),
            ],
        ),
    ]
