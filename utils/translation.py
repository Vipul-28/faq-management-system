

from googletrans import Translator

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
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return text
