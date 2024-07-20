from django.db import models

class Review(models.Model):
    retailer = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    review = models.TextField()
    aspect = models.CharField(max_length=255)
    aspect_sentiment = models.FloatField()
    overall_sentiment = models.IntegerField()
    scrape_date = models.CharField(max_length=255)
    stars_count = models.FloatField()
