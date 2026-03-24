import pytest

from src.domain.text_processor import get_lemma

@pytest.mark.parametrize(
    "word, expected",
    [
        ("Бежал", "бежать"),
        ("бегущей", "бежать"),
        ("собаки!", "собака"),
        ("123", ""),
        ("Весело", "весело"),
    ],
)
def test_get_lemma(word, expected):
    assert get_lemma(word) == expected
