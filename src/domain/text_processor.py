import re

import pymorphy3

from src.domain.constants import WORD_CLEANUP_PATTERN

morph = pymorphy3.MorphAnalyzer()

def get_lemma(word: str) -> str:
    clean_word = re.sub(WORD_CLEANUP_PATTERN, "", word).lower()

    if not clean_word:
        return ""

    parsed = morph.parse(clean_word)[0]

    return parsed.normal_form