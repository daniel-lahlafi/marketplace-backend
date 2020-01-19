from django.conf.urls import url
from django.urls import path
from .views import ListingListView

urlpatterns = [
    path('listings/<str:pk>', ListingListView.as_view()),
    url('listings', ListingListView.as_view(), name='listings'),
]
