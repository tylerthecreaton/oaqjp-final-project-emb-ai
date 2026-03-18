"""Flask server for the Emotion Detector application."""

from __future__ import annotations

from flask import Flask, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page() -> str:
    """Render the application home page."""
    return app.send_static_file("index.html")


@app.route("/emotionDetector")
def sent_detector() -> str:
    """Run emotion detection for user input and format the response."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please try again!."

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
