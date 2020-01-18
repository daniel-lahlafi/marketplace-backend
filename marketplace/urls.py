from django.conf.urls import url
from .views import ListingListView

urlpatterns = [
  	url('listings', ListingListView.as_view(), name='listings'),
]