from django.urls import path, include
from rest_framework import routers
from ..Views import RoutineViewSet

Router = routers.DefaultRouter()
Router.register(r'Routine', RoutineViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
