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



#### 1. 🚀 Clone the Repository

```bash
git clone https://github.com/adarsh2023calc/LocEnergy2.0.git
cd LocEnergy2.0 

#### 2. 🔐 Install Dependencies & Create `.env` File

Install the required Python dependencies:

```bash
pip install -r requirements.txt```

docker build -t locenergy-app .
docker run -p 8080:8080 locenergy-app


This version ensures:
- Each command block is properly closed.
- Markdown renders cleanly with separated steps.
- You follow standard `README.md` heading practices.

Let me know if you want to add `.env` file example or any Gemini-specific setup tips!

