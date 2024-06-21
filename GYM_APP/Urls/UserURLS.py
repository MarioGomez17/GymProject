from django.urls import path, include
from rest_framework import routers
from ..Views import UserViewSet

Router = routers.DefaultRouter()
Router.register(r'User', UserViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
