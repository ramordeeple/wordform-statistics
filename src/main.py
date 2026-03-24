import uvicorn
from fastapi import FastAPI

from src.api.report import router
from src.core.settings import settings

app = FastAPI(title="Wordform statistics", debug=settings.DEBUG)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.DEBUG
    )