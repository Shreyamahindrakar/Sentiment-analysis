# Generated by Django 5.0.7 on 2024-07-20 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retailer', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('review', models.TextField()),
                ('aspect', models.CharField(max_length=255)),
                ('aspect_sentiment', models.FloatField()),
                ('overall_sentiment', models.IntegerField()),
                ('scrape_date', models.CharField(max_length=255)),
                ('stars_count', models.FloatField()),
            ],
        ),
    ]
