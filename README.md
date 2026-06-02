# PDF to Markdown Converter

A simple FastAPI application that converts uploaded PDF files into Markdown using Microsoft's MarkItDown.

## Features

- Upload PDF files
- Convert PDF → Markdown
- Download generated Markdown
- Simple web interface
- FastAPI backend

## Installation

### Clone repository

```bash
git clone https://github.com/yourusername/pdf-to-markdown.git
cd pdf-to-markdown
```

### Create virtual environment

```bash
python -m venv venv
```

Activate:

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run locally

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## API

### Convert PDF

POST

```text
/convert
```

Form field:

```text
file
```

Returns:

```json
{
  "success": true,
  "download_url": "/download/uuid"
}
```

### Download Markdown

GET

```text
/download/{file_id}
```

## Deployment

### Render

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

### Railway

Works without modification.

## Powered By

- FastAPI
- Microsoft MarkItDown
