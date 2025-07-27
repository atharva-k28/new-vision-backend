# 🖼️ Image Description API - FastAPI Backend

This is a FastAPI Python backend that processes image files to generate:

- 🧠 **Image captions** using Salesforce BLIP  
- 🔍 **OCR text extraction** using Tesseract OCR  

Send an image to the API, and receive a smart description and any text detected in the image.

---

## ⚙️ Tech Stack

- **FastAPI** (Web framework)  
- **Salesforce BLIP** (Image captioning via Hugging Face Transformers)  
- **Tesseract OCR** (for reading text from images)  
- **CORS Middleware** (for frontend compatibility)  

---

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
## 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```
Make sure Tesseract is installed and accessible in your system path:

Ubuntu:

```bash
sudo apt install tesseract-ocr
```
macOS:
```bash
brew install tesseract
```
Windows:
Download from: https://github.com/tesseract-ocr/tesseract

## 🚀 3. Run Locally
Your FastAPI app entry point is app/main.py. 
To start the server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
Access it at: http://localhost:8000

## 🧠 4.API Endpoints

POST /process-image
Takes an image file and returns a caption (and OCR if applicable).

Request: multipart/form-data with image file

Response:

```json
{
  "caption": "A man holding a sign. It says: Hello World!"
}
```

POST /process-url
Takes a direct image URL.

Request:

```json
{
  "img_url": "https://example.com/image.jpg"
}
```
Response:

```json
{
  "caption": "A dog playing in a park."
}
```
## 🌐 5.Frontend Integration (Fixing CORS Error)
If you're using a hosted frontend like Vercel, the browser may block requests due to HTTP (backend) vs HTTPS (frontend).

To fix this, tunnel your local backend using ngrok.

🔧 Using ngrok
Install ngrok: https://ngrok.com/download

Run the tunnel:

```bash
ngrok http 8000
```
Use the https://... URL provided by ngrok in your frontend requests.

## ✅ 6.CORS Settings in Backend
CORS is already enabled in main.py for:

http://localhost:5173
https://new-vision-frontend-react.vercel.app
