# Generated by Django 4.0.3 on 2022-05-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('address', models.TextField(max_length=300)),
                ('phone_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('address', models.TextField(max_length=300)),
                ('phone_no', models.IntegerField()),
            ],
        ),
    ]