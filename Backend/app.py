from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import shutil

from src.mission.runner import MissionRunner

app = FastAPI(
    title="Chandrayaan-2 Mission Planner API",
    version="1.0.0",
    description="Backend API for Lunar Ice Detection and Mission Planning"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

# Serve generated images
app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")


@app.get("/")
def home():
    return {
        "message": "Chandrayaan-2 Mission Planner API",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


@app.post("/upload")
async def upload_dataset(
    ohrc: UploadFile = File(...),
    ohrc_xml: UploadFile = File(...),
    tmc: UploadFile = File(...),
    sar: UploadFile = File(...)
):

    files = [
        ohrc,
        ohrc_xml,
        tmc,
        sar,
    ]

    for file in files:

        file_path = UPLOAD_DIR / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Files uploaded successfully"
    }


@app.post("/analyze")
def analyze():

    img_files = list(UPLOAD_DIR.glob("*.img"))
    xml_files = list(UPLOAD_DIR.glob("*.xml"))

    if not img_files:
        return {
            "error": "No OHRC image uploaded."
        }

    if not xml_files:
        return {
            "error": "No OHRC XML uploaded."
        }

    runner = MissionRunner()

    result = runner.run(
        img_files[0],
        xml_files[0]
    )

    return result