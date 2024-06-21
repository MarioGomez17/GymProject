from django.urls import path, include
from rest_framework import routers
from ..Views import WeightUnitViewSet

Router = routers.DefaultRouter()
Router.register(r'', WeightUnitViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
