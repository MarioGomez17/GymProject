from django.urls import path, include
from rest_framework import routers
from ..Views import ExerciseTypeViewSet

Router = routers.DefaultRouter()
Router.register(r'', ExerciseTypeViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
