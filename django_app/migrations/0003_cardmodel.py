# Generated by Django 4.2.1 on 2023-07-04 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_filemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='cardmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('discript', models.CharField(max_length=30)),
                ('file', models.FileField(upload_to='django_app/static')),
            ],
        ),
    ]