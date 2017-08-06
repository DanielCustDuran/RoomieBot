from googletrans import Translator

translator = Translator()

def detect_lang(sent_exmp):
	trans_list = translator.detect(sent_exmp)
	return trans_list.lang

def translator_lang_en(sentence, dest = 'en'):
	text_traducted = translator.translate(sentence, dest)
	return text_traducted.text

def translator_lang_esp(sentence, dest = 'es'):
	text_traducted = translator.translate(sentence, dest)
	return text_traducted.text