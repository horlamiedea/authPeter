# Generated by Django 2.2.18 on 2021-03-25 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=60)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
