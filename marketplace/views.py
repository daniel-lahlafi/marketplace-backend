from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import ListingSerializer
from .models import Listing


class ListingListView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        search_terms = request.GET.get('search', None)
        user = request.GET.get('user', None)

        if user == None:
            listings = Listing.objects.all()
        else:
            listings = Listing.objects.filter(author_email=user)

        serializer = ListingSerializer(listings, many=True)
        for listing_entry in serializer.data:
            listing_entry["listing_image"] = request.build_absolute_uri('/')[:-1].strip("/") + \
                                             listing_entry["listing_image"]

        # if search_terms is not None:
        #     serializer.data = [listing for listing in serializer.data if search_terms in listing["listing_title"]]

        return Response([listing for listing in serializer.data if search_terms in listing["listing_title"]] if
                        search_terms is not None else serializer.data)


    def post(self, request, *args, **kwargs):
        file_serializer = ListingSerializer(data=request.data)
        print(file_serializer)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        print(pk)
        listing = Listing.objects.get(listing_id=pk)
        listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)