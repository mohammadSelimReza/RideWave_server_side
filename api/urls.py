from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('user',views.UserViewSet,basename='user_list')

urlpatterns = [
    path("",include(router.urls)),
    path("token/",TokenObtainPairView.as_view(),name="get_token"),
    path("token/refresh/",TokenRefreshView.as_view(),name='refresh'),
    path("api-auth/",include("rest_framework.urls")),
    path('update-password/', views.UserPasswordUpdateView.as_view(), name='update-password'),
]
