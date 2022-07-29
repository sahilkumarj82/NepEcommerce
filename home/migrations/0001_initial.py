# Generated by Django 4.0.6 on 2022-07-26 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdsBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media')),
                ('label', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('BannerRank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=200)),
                ('slug', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PopupNewsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media')),
                ('discount_per', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media')),
                ('topic', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('price', models.FloatField(blank=True)),
                ('rank', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('active', 'Active'), ('', 'Default')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(blank=True, max_length=200)),
                ('slug', models.TextField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(default=0)),
                ('image1', models.ImageField(upload_to='media')),
                ('image2', models.ImageField(upload_to='media')),
                ('brief_Description', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('specification', models.TextField(blank=True)),
                ('shipping', models.TextField(blank=True)),
                ('slug', models.TextField(unique=True)),
                ('labels', models.CharField(choices=[('dealDay', 'DealDay'), ('new', 'New'), ('hot', 'Hot'), ('sale', 'Sale'), ('', 'default')], max_length=100)),
                ('stock', models.CharField(choices=[('In Stock', 'In Stock'), ('Out Stock', 'Out Stock')], max_length=100)),
                ('brand', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subcategory')),
            ],
        ),
    ]