from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
from dotenv import load_dotenv
import math

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_SOLAR_API_KEY")  # store your key in .env

app = FastAPI()

# CORS setup for frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predict")
async def predict_solar_energy(lat: float = Query(...), lng: float = Query(...)):

    url = (
        f"https://solar.googleapis.com/v1/buildingInsights:findClosest"
        f"?location.latitude={lat}&location.longitude={lng}&requiredQuality=HIGH&key={GOOGLE_API_KEY}"
    )
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        print("Hello World for everyone")

    return data
