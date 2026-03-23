import pymorphy3

from src.domain.constants import WORD_CLEANUP_PATTERN

morph = pymorphy3.MorphAnalyzer()

def get_lemma(word: str) -> str:
    clean_word = WORD_CLEANUP_PATTERN.sub('', word.lower())

    if not clean_word or clean_word.isdigit():
        return ""

    parsed = morph.parse(clean_word)

    return parsed[0].normal_form