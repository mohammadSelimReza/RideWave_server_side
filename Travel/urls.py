from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views


router = DefaultRouter()

router.register('request/list',views.UserRequestView,basename='request_list')
router.register('request/detail',views.TravelDetailsView,basename='ride_details')
router.register('request/history',views.TravelHistoryView,basename='ride_history')

urlpatterns = [
    path("",include(router.urls)),
    path('request/end_ride/<int:request_no>/', views.EndRideView.as_view(), name='end_ride'),
]