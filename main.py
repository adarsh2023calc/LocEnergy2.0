from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
from dotenv import load_dotenv
import json
import requests
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



@app.get("/place_info")
async def fetch_place_info(lat: float = Query(...), lng: float = Query(...)):

    try:
        url = (
            f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
            f"location={lat},{lng}&radius=1000&type=restaurant&key={GOOGLE_API_KEY}"
        )

        
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()

        print(data)
        return data
    except:
         return httpx.RequestError("Failure! Unable to extract data")


@app.get("/get_gemini_suggest")


async def get_gemini_suggest(items: str= Query(...)):
    prompt = f"""
    Here is a data:
    {json.dumps(items, indent=2)}

    From the data, gather insights and display them clearly.
    """

    

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    result = response.json()
    print(result)
    output = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No output received")

    return {"output": output}