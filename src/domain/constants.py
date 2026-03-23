# Бизнес константы

import re

from typing import Final

WORD_CLEANUP_PATTERN: Final[re.Pattern] = re.compile(r'[^а-яА-ЯёЁa-zA-Z]')
TEXT_ENCODING: Final[str] = "utf-8"
ALLOWED_EXTENSION: Final[str] = ".txt"

COLUMN_WORD: Final[str] = "Словоформа"
COLUMN_TOTAL: Final[str] = "Всего во всем документе"
COLUMN_PER_LINE: Final[str] = "Кол-во в каждой из строк"