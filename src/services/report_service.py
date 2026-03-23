import uuid
from pathlib import Path
from typing import BinaryIO, Counter, Tuple, Dict, List

from src.infrastructure.excel_writer import write_frequency_report
from src.core import settings
from src.core.constants import REPORT_EXTENSION
from src.domain.constants import TEXT_ENCODING
from src.domain.text_processor import get_lemma


class ReportService:
    def __init__(self):
        pass

    def execute_export(self, file_stream: BinaryIO) -> str:
        global_stats, lines_stats = self._analyze_text(file_stream)
        output_path = self._generate_report_path()
        write_frequency_report(global_stats, lines_stats, output_path)

        return output_path

    @staticmethod
    def _generate_report_path() -> str:
        file_id = str(uuid.uuid4())
        full_path = Path(settings.FILE_REPORT_DIR) / f"{file_id}{REPORT_EXTENSION}"
        full_path.parent.mkdir(parents=True, exist_ok=True)

        return str(full_path)

    @staticmethod
    def _analyze_text(file_stream: BinaryIO) -> Tuple[Counter, List[Dict[str, int]]]:
        global_counter = Counter()
        line_counters: List[Dict[str, int]] = []

        for line_bytes in file_stream:
            try:
                line_str = line_bytes.decode(TEXT_ENCODING)
            except UnicodeDecodeError:
                continue

            # Разбиение строки на слова и лемматизация
            words = (w.strip() for w in line_str.split())
            lemmas = [get_lemma(w) for w in words if w]

            # Фильтрация пустых результатов (когда слово состоит только из символов)
            valid_lemmas = [l for l in lemmas if l]

            # Подсчет слов в текущей строке
            current_lines_stats = Counter(valid_lemmas)
            # Обновление статистики всего документа
            global_counter.update(current_lines_stats)
            # Сохранение статистики конкретной строки
            line_counters.append(dict(current_lines_stats))

        return global_counter, line_counters