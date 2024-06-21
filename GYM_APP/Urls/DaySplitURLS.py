from django.urls import path, include
from rest_framework import routers
from ..Views import DaySplitViewSet

Router = routers.DefaultRouter()
Router.register(r'', DaySplitViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
