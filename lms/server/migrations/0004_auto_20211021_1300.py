# Generated by Django 3.2.6 on 2021-10-21 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20211020_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(default='Unassigned', max_length=100),
        ),
        migrations.AlterField(
            model_name='record',
            name='issue_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
