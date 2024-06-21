from django.urls import path, include
from rest_framework import routers
from ..Views import ExerciseRoutineTemplateViewSet

Router = routers.DefaultRouter()
Router.register(r'ExerciseRoutineTemplate', ExerciseRoutineTemplateViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
