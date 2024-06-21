from django.urls import path, include
from rest_framework import routers
from ..Views import ExerciseViewSet

Router = routers.DefaultRouter()
Router.register(r'', ExerciseViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
