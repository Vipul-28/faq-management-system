
# utils/translation.py

from googletrans import Translator

# Initialize the translator object
translator = Translator()

def translate_text(text, target_language='en'):
    """
    Translates the given text into the target language.
    
    :param text: The text to be translated
    :param target_language: The language to translate the text to (default: 'en' for English)
    :return: Translated text or the original text if translation fails
    """
    try:
        if not text:
            return text
        # Perform translation
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return text  # Fallback to the original text in case of error
