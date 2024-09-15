# Generated by Django 4.1.3 on 2024-09-15 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('liquor_id', models.CharField(max_length=50)),
                ('ingredient_id', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.CharField(default='default_image_url.jpg', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=200)),
                ('admin', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderBeverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beverage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dranksforyou2api.beverage')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dranksforyou2api.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dranksforyou2api.user'),
        ),
        migrations.CreateModel(
            name='Liquor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(default='default_image_url.jpg', max_length=100)),
                ('uid', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='dranksforyou2api.user')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(default='default_image_url.jpg', max_length=100)),
                ('uid', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='dranksforyou2api.user')),
            ],
        ),
        migrations.AddField(
            model_name='beverage',
            name='uid',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='dranksforyou2api.user'),
        ),
    ]
