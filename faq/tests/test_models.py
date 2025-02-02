from rest_framework.test import APITestCase
from rest_framework import status
from .models import FAQ

class FAQApiTest(APITestCase):

    def setUp(self):
        FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python framework."
        )

    def test_faq_list(self):
        response = self.client.get('/api/faqs/?lang=en')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['question'], "What is Django?")
