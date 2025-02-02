from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import FAQ
from .serializers import FAQSerializer

class FAQPagination(PageNumberPagination):
    page_size = 10  # Adjust this value as per your need

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    pagination_class = FAQPagination

    def list(self, request, *args, **kwargs):
        lang = request.GET.get('lang', 'en')
        queryset = self.get_queryset()
        data = [faq.get_translation(lang) for faq in queryset]
        return Response(data)
