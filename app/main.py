import uvicorn
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
#from transformers import pipeline, AutoProcessor
#from PIL import Image
#from io import BytesIO

class Text(BaseModel):
    input_text:str

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
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

#processor=AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base",use_fast=True)
#captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base",image_processor=processor)

@app.post("/process-url")
def process_url(data: url):
    #caption = captioner(data.img_url)
    #return{"caption":caption[0]['generated_text']}
    return {"caption":"test-caption"}

@app.post("/process-image")
async def process_image(file:UploadFile = File(...)):
    #contents = await file.read()
    #image = Image.open(BytesIO(contents))
    #caption = captioner(image)
    #return {"caption":caption[0]['generated_text']}
    return {"caption":"test-caption"}
