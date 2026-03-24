from io import BytesIO
from src.services.report_service import ReportService


def test_report_service_logic():
    service = ReportService()

    content = "Бежать бежать.\nБежал бегун."
    file_stream = BytesIO(content.encode("utf-8"))

    global_stats, lines_stats = service._analyze_text(file_stream)

    assert global_stats["бежать"] == 3
    assert global_stats["бегун"] == 1

    # Проверяем построчную статистику
    assert len(lines_stats) == 2
    assert lines_stats[0]["бежать"] == 2
    assert lines_stats[1]["бежать"] == 1
