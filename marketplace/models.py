from django.db import models

class Listing(models.Model):
    author_email = models.EmailField()
    author_name = models.CharField()
    listing_title = models.CharField()
    listing_description = models.TextField()
    listing_price = models.FloatField()
    pub_date = models.DateTimeField()
    
class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    image = models.BinaryField()
