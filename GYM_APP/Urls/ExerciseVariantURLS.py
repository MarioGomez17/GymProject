from django.urls import path, include
from rest_framework import routers
from ..Views import ExerciseVariantViewSet

Router = routers.DefaultRouter()
Router.register(r'', ExerciseVariantViewSet)

urlpatterns = [
    path('', include(Router.urls))
]
