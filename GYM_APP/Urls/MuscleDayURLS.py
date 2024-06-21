from django.urls import path, include
from rest_framework import routers
from ..Views import MuscleDayViewSet

Router = routers.DefaultRouter()
Router.register(r'MuscleDay', MuscleDayViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
