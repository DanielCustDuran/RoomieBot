import nltk
from translator import translator_lang_en, translator_lan_es

def get_tokens(sentence):
	tokens = nltk.word_tokenize(sentence.lower())
	tagged = nltk.pos_tag(tokens)

get_tokens(translator_lang_en("HOLA, QUIERO IR A CIUDAD DE MEXICO"))