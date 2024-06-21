from django.urls import path, include
from rest_framework import routers
from ..Views import SplitViewSet

Router = routers.DefaultRouter()
Router.register(r'Split', SplitViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
