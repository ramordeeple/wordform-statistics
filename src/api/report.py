from fastapi import APIRouter, UploadFile, File, HTTPException, status
from starlette.responses import FileResponse

from src.core.constants import REPORT_EXTENSION, REPORT_MIME_TYPE
from src.domain.constants import ALLOWED_EXTENSION
from src.services.report_service import ReportService

router = APIRouter(prefix="/public/reports")

@router.post("/export")
async def export_word_stats(file: UploadFile = File(...)):
    """
    Принимает .txt файл и возвращает Excel-отчет с частотой словоформ.
    :param file: .txt файл (также поддерживаются большого объема)
    :return: .xlsx со статистикой
    """

    if not file.filename.endswith(ALLOWED_EXTENSION):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Допускаются только .txt"
        )

    service = ReportService()

    try:
        report_path = service.execute_export(file.file)
        download_name = f"frequency_report{REPORT_EXTENSION}"

        return FileResponse(
            path=report_path,
            filename=download_name,
            media_type=REPORT_MIME_TYPE
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ошибка при обработке файла: {str(e)}"
        )

    finally:
        await file.close()