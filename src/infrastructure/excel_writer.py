from typing import Counter, List, Dict
import pandas as pd

from src.domain.constants import COLUMN_WORD, COLUMN_PER_LINE, COLUMN_TOTAL


def write_frequency_report(
    global_stats: Counter,
    lines_stats: List[Dict[str, int]],
    output_path: str,
) -> None:
    """
    Записывает собранную статистику в формат Excel.

    :param global_stats: Общий счетчик слов по всему документу.
    :param lines_stats: Список словарей (счетчик для каждой строки).
    :param output_path: Полный путь для сохранения .xlsx файла.
    """

    def generate_rows():
        for word, total_count in global_stats.items():
            counts_per_line = ",".join(str(line.get(word, 0)) for line in lines_stats)

        yield {
            COLUMN_WORD: word,
            COLUMN_TOTAL: total_count,
            COLUMN_PER_LINE: counts_per_line
        }

    df = pd.DataFrame(generate_rows())
    df.to_excel(output_path, index=False, engine="openpyxl")