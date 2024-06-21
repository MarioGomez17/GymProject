from django.urls import path, include
from rest_framework import routers
from ..Views import RoutineTemplateViewSet

Router = routers.DefaultRouter()
Router.register(r'RoutineTemplate', RoutineTemplateViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
