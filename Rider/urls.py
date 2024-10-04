from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views


router = DefaultRouter()

router.register('list',views.RiderRegistrationView,basename='rider_list')
router.register('user',views.UserView,basename='user')
router.register('register',views.RiderRegistrationView,basename='rider_register')

urlpatterns = [
    path("",include(router.urls)),
    # path("register/",views.RiderRegistrationView.as_view(),name='rider_register')
]