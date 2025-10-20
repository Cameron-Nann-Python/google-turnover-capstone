from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from app.routes import router

DATA_PATH = Path("csv")
MODEL_PATH = Path("models")

app = FastAPI(title="Salifort Motors Employee Turover API")
@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head><title>Employee Turnover API</title></head>
        <body>
            <h2>Salifort Motors Employee Turnover Prediction API</h2>
            <p><a href="/docs"><button>Swagger Docs</button></a></p>
        </body>
    </html>
    """

app.include_router(router=router)
