from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet

router = DefaultRouter()
router.register('faqs', FAQViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
