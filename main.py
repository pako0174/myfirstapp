
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

PIXABAY_API_KEY = "22581550-bf6ccdce74a200fef76fb2b2d"

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, keyword: str = Form(...)):
    response = requests.get("https://pixabay.com/api/", params={
        "key": PIXABAY_API_KEY,
        "q": keyword,
        "per_page": 25,
        "image_type": "photo",
        "safesearch": "true"
    })
    data = response.json()
    images = data.get("hits", [])
    return templates.TemplateResponse("result.html", {"request": request, "images": images, "keyword": keyword})
