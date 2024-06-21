from django.urls import path, include
from rest_framework import routers
from ..Views import ExerciseEquipmentViewSet

Router = routers.DefaultRouter()
Router.register(r'', ExerciseEquipmentViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
