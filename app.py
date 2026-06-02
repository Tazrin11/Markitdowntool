from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from markitdown import MarkItDown

import os
import uuid

app = FastAPI(title="PDF to Markdown Converter")

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/convert")
async def convert_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Only PDF files are supported"}

    unique_id = str(uuid.uuid4())

    pdf_path = os.path.join(
        UPLOAD_DIR,
        f"{unique_id}.pdf"
    )

    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    md = MarkItDown()

    result = md.convert(pdf_path)

    output_path = os.path.join(
        OUTPUT_DIR,
        f"{unique_id}.md"
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result.text_content)

    return {
        "success": True,
        "download_url": f"/download/{unique_id}"
    }


@app.get("/download/{file_id}")
async def download_markdown(file_id: str):

    md_file = os.path.join(
        OUTPUT_DIR,
        f"{file_id}.md"
    )

    if not os.path.exists(md_file):
        return {"error": "File not found"}

    return FileResponse(
        path=md_file,
        filename="converted.md",
        media_type="text/markdown"
    )
