from django.urls import path, include
from rest_framework import routers
from ..Views import MuscleViewSet

Router = routers.DefaultRouter()
Router.register(r'Muscle', MuscleViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
