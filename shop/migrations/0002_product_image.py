# Generated by Django 2.2.4 on 2019-11-18 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='produts/%Y/%m/%d'),
        ),
    ]
