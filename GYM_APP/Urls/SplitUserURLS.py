from django.urls import path, include
from rest_framework import routers
from ..Views import SplitUserViewSet

Router = routers.DefaultRouter()
Router.register(r'SplitUser', SplitUserViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
