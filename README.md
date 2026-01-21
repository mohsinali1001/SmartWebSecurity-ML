# DigitalAxis Web Attack Detection ML

**DigitalAxis Web Attack Detection ML** is a machine learning-powered system that monitors network traffic and user behavior to detect potential web attacks in real-time. It provides actionable insights and automated session protection, making web applications more secure against malicious activity.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
This project implements a predictive ML model to identify suspicious web activity based on various features such as network packet size, protocol type, login attempts, session duration, encryption usage, IP reputation, browser type, and unusual access times. It is designed to integrate seamlessly with web applications, providing both predictions and probabilities of potential attacks.

---

## Features
- Real-time web attack detection using ML
- Prediction and probability scores for suspicious activity
- Supports automated session lock if an attack is detected
- REST API built with FastAPI for easy integration
- CORS enabled for cross-origin requests
- Health check endpoint to ensure model is loaded and running

---

## Technology Stack
- **Backend Framework:** FastAPI
- **Machine Learning:** Scikit-learn / Python ML pipelines
- **Serialization:** Pickle
- **Database (optional for extended functionality):** PostgreSQL
- **Deployment:** Local, Docker, or cloud services like Render
- **Version Control:** Git & GitHub

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ml-web-attack-api.git
   cd ml-web-attack-api
Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
Install dependencies:

pip install -r requirements.txt
Make sure your model file (pipe.pkl) is in the model/ folder.

Usage
Start the FastAPI server:

python -m uvicorn app:app --host 0.0.0.0 --port 8000
Once running, you can access:

API docs: http://localhost:8000/docs

Health check: http://localhost:8000/health

API Endpoints
Root
GET /

Returns the service status and whether the model is loaded.

Predict
POST /predict

Accepts JSON payload with the following fields:

{
  "network_packet_size": 100.5,
  "protocol_type": "TCP",
  "login_attempts": 3,
  "session_duration": 120.0,
  "encryption_used": "AES",
  "ip_reputation_score": 0.85,
  "failed_logins": 1,
  "browser_type": "Chrome",
  "unusual_time_access": 0
}
Returns prediction, probability, and attack detection status.

Health
GET /health

Returns the health of the API and model status.

Contributing
Contributions, issues, and feature requests are welcome!
Feel free to fork the repository and submit pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for details.
