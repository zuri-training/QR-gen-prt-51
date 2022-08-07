
from django.urls import path, include
from rest_framework import routers
from .views import QrcodeApiViewSet


router = routers.DefaultRouter()
router.register('basic', QrcodeApiViewSet)
urlpatterns = [
    path('', include(router.urls))
]
