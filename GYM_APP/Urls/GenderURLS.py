from django.urls import path, include
from rest_framework import routers
from ..Views import GenderViewSet

Router = routers.DefaultRouter()
Router.register(r'', GenderViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
