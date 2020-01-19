from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import ListingSerializer
from .models import Listing


class ListingListView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)
        print()
        for listing_entry in serializer.data:
            listing_entry["listing_image"] = request.build_absolute_uri('/')[:-1].strip("/") + \
                                             listing_entry["listing_image"]

        print(serializer.data)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        file_serializer = ListingSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
