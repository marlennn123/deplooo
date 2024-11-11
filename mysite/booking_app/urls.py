from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hotels', HotelListViewSet, basename='hotel-list'),
router.register(r'hotel-detail', HotelDetailViewSet, basename='hotel-detail')
router.register(r'users', UserProfileViewSet, basename='user-list')
router.register(r'room', RoomListViewSet, basename='room-list')
router.register(r'room-detail', RoomDetailViewSet, basename='room-detail')
router.register(r'booking', BookingViewSet, basename='book-list')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'room-images', RoomImageViewSet, basename='room-images')


urlpatterns = [
    path('', include(router.urls))
]


