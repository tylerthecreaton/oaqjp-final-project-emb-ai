"""Utilities for emotion detection using Watson NLP service."""

from __future__ import annotations

from typing import Any

import requests

WATSON_ENDPOINT = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
WATSON_HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def _none_emotion_response() -> dict[str, Any]:
    """Return the response shape used when analysis cannot be performed."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def emotion_detector(text_to_analyze: str) -> dict[str, Any]:
    """Analyze input text and return emotions and dominant emotion."""
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            WATSON_ENDPOINT,
            json=payload,
            headers=WATSON_HEADERS,
            timeout=10,
        )
    except requests.RequestException:
        return _none_emotion_response()

    if response.status_code == 400:
        return _none_emotion_response()

    if response.status_code != 200:
        return _none_emotion_response()

    response_json = response.json()
    emotions = response_json["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion,
    }
