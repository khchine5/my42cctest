# Generated by Django 2.1.1 on 2018-09-30 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='First name')),
                ('surname', models.CharField(max_length=50, verbose_name='Second name')),
                ('date_birth', models.DateField(verbose_name='Date of Birth')),
                ('bio', models.TextField(max_length=1000, verbose_name='bio')),
                ('contact', models.TextField(max_length=255, verbose_name='contact')),
            ],
        ),
    ]