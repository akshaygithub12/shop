# Generated by Django 3.2 on 2021-06-22 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50)),
                ('img1', models.ImageField(default='', upload_to='b1/images')),
                ('header1', models.CharField(max_length=50)),
                ('img2', models.ImageField(default='', upload_to='b1/images')),
                ('img3', models.ImageField(default='', upload_to='b1/images')),
                ('header3', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
