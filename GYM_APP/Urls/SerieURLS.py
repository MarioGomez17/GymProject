from django.urls import path, include
from rest_framework import routers
from ..Views import SerieViewSet

Router = routers.DefaultRouter()
Router.register(r'Serie', SerieViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
