from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['author_email', 'author_name', 'listing_title', 'listing_description', 'listing_price', 'pub_date']