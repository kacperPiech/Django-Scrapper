from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WebsiteContentViewSet

router = DefaultRouter()
router.register(r"WebsiteContents", WebsiteContentViewSet, basename="WebsiteContent")

urlpatterns = [
    path('', include(router.urls)),
]