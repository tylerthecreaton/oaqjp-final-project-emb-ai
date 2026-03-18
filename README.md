# Emotion Detector Flask App

This project analyzes emotions from user text using an IBM Watson NLP endpoint and serves a web UI with Flask.

## Features

- Emotion detection with anger, disgust, fear, joy, sadness
- Dominant emotion calculation
- Flask endpoint for browser-based interaction
- Unit tests for expected behavior and error handling
- Static analysis support via pylint

## Run locally

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start server:

   ```bash
   python server.py
   ```

3. Open `http://127.0.0.1:5000`.
