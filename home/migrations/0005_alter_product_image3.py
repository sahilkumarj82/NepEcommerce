# Generated by Django 4.0.6 on 2002-07-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(upload_to='media'),
        ),
    ]
