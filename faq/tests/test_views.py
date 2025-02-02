from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):

    def test_get_translation(self):
        faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python framework.",
            question_hi="Django kya hai?",
            answer_hi="Django ek Python framework hai."
        )

        self.assertEqual(faq.get_translation('en'), {'question': "What is Django?", 'answer': "Django is a Python framework."})

        self.assertEqual(faq.get_translation('hi'), {'question': "Django kya hai?", 'answer': "Django ek Python framework hai."})
