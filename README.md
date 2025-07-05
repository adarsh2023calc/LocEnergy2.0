# ☀️ LocEnergy 2.0

A FastAPI-powered web application that estimates solar energy potential and installation costs for a given location using Google’s Solar and Places APIs, and integrates Gemini AI for smart insights.

---

## 🚀 Features

- 🌍 Get solar energy data by providing **latitude and longitude**
- 🏢 Retrieve nearby **place information** using Google Places API
- 🤖 Generate AI-based cost estimates using **Gemini Pro (Google’s LLM)**
- ⚙️ FastAPI backend with RESTful routes
- 🐳 Dockerized for easy deployment
- ☁️ Deployed on **Google Cloud Run** with CI/CD via Cloud Build

---

## 🧰 Tech Stack

| Layer       | Technology                      |
|-------------|----------------------------------|
| Backend     | Python, FastAPI                 |
| AI          | Gemini Pro (via REST API)       |
| External APIs | Google Solar API, Places API   |
| Deployment  | Docker, Cloud Build, Cloud Run  |
| Env Mgmt    | python-dotenv                   |
| Frontend    | HTML + Tailwind CSS (served via StaticFiles) |

---

## 📦 API Endpoints

### `GET /predict`
Fetch solar building insights for a location.

**Query Parameters:**
- `lat`: Latitude (float)
- `lng`: Longitude (float)

---

### `GET /place_info`
Get nearby restaurants (or places) for the specified location.

**Query Parameters:**
- `lat`: Latitude (float)
- `lng`: Longitude (float)

---

### `GET /get_gemini_suggest`
Use Gemini AI to generate insights based on solar data and location.

**Query Parameters:**
- `items`: Raw JSON string from the Solar API
- `lat`: Latitude (float)
- `lng`: Longitude (float)

---

## 🛠️ Local Development

### 🔧 Prerequisites
- Python 3.10+
- Docker (optional)
- Google API keys
- Gemini Pro API key

### 🧪 Setup Steps

1. **Clone the repository**

```bash
git clone https://github.com/adarsh2023calc/LocEnergy2.0.git
cd LocEnergy2.0```

2. **Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Create .env file

bash
Copy
Edit
GOOGLE_SOLAR_API_KEY=your_google_api_key
GEMINI_API_KEY=your_gemini_api_key
Run the app

bash
Copy
Edit
uvicorn main:app --reload
Open in browser

cpp
Copy
Edit
http://127.0.0.1:8000
🐳 Docker Deployment
bash
Copy
Edit
docker build -t locenergy-app .
docker run -p 8080:8080 locenergy-app 
