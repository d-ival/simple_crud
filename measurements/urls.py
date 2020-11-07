from django.urls import path, include
from measurements.views import ProjectViewSet, MeasurementViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'measurements', MeasurementViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
