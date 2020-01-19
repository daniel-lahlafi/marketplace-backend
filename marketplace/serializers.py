from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['listing_id', 'author_email', 'author_name', 'listing_title', 'listing_description', 'listing_price',
                  'listing_image', 'pub_date']
