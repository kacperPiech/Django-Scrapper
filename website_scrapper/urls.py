from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WebsiteContentViewSet

router = DefaultRouter()
router.register(r"Articles", WebsiteContentViewSet, basename="Article")

urlpatterns = [
    path('', include(router.urls)),
]