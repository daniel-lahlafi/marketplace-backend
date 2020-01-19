from django.db import models
import uuid


def upload_location(instance, filename):
    return f"image/{uuid.uuid4()}.{filename.split('.')[-1]}"


class Listing(models.Model):
    listing_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    author_email = models.EmailField()
    author_name = models.CharField(max_length=50)
    listing_title = models.CharField(max_length=140)
    listing_description = models.TextField()
    listing_price = models.FloatField()
    listing_image = models.ImageField(upload_to=upload_location)
    pub_date = models.DateTimeField(auto_now_add=True)
