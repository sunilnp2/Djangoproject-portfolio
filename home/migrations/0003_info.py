# Generated by Django 3.2 on 2021-05-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField(max_length=300)),
                ('street', models.TextField(max_length=300)),
                ('time', models.TextField(max_length=300)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=300)),
            ],
        ),
    ]