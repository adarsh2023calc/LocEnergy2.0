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

    try:
        url = (
            f"https://solar.googleapis.com/v1/buildingInsights:findClosest"
            f"?location.latitude={lat}&location.longitude={lng}&requiredQuality=HIGH&key={GOOGLE_API_KEY}"
        )

        
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()

        
        return data
    except:
         return httpx.RequestError("Failure! Unable to extract data")



@app.post("/predict_nasa")
async def predict_energy_from_Nasa(lat: float = Query(...), lng: float = Query(...)):
    nasa_api=f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_SW_DWN&community=RE&longitude={lat}&latitude={lng}&start=20240101&end=20241231&format=JSON"
    async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()

    return data



