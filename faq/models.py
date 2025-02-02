from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from utils.translation import translate_text  # Import the translation function

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    def get_translation(self, lang):
        """Dynamically translates question and answer, with Redis caching."""
        cache_key = f"faq_translation_{self.id}_{lang}"
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation  

        translated_data = {
            'question': translate_text(self.question, lang),
            'answer': translate_text(self.answer, lang),
        }

        cache.set(cache_key, translated_data, timeout=3600)
        
        return translated_data

    def __str__(self):
        return self.question
