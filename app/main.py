import uvicorn
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline, AutoProcessor
import pytesseract
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

class Text(BaseModel):
    input_text:str

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","https://new-vision-frontend-react.vercel.app"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
def read_root():
    return {"message":"Hello World!"}

@app.get("/text")
def read_text():
    return{"text":"static_text"}

@app.post("/process-text")
def process_text(data: Text):
    text=data.input_text
    text+=" - OK RECEIVED!"
    return {"received":text}

class url(BaseModel):
    img_url:str

processor=AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base",use_fast=True)
captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base",image_processor=processor)

ocr_keywords=["text","sign","poster","handwritten","handwriting","writing","caption","note","message"]

def extract_ocr_text_from_pil(image: Image.Image) -> str:
    img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

    raw_text = pytesseract.image_to_string(gray, config="--oem 3 --psm 6")

    cleaned = '\n'.join([line.strip() for line in raw_text.split('\n') if len(line.strip()) > 3])
    return cleaned

@app.post("/process-url")
def process_url(data: url):
    caption = captioner(data.img_url)
    return{"caption":caption[0]['generated_text']}

@app.post("/process-image")
async def process_image(file:UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(BytesIO(contents))
    caption = captioner(image)
    caption=caption[0]['generated_text']
    if any(word in caption.lower() for word in ocr_keywords):
        ocr_text = extract_ocr_text_from_pil(image=image)
        caption+=f'It says: {ocr_text}'
    return {"caption":caption}
