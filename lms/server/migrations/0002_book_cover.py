# Generated by Django 3.2.6 on 2021-10-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='book_cover/%Y/%m/%d'),
        ),
    ]