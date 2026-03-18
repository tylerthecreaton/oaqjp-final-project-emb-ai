"""Unit tests for the EmotionDetection package."""

from __future__ import annotations

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verify dominant emotion mapping and error handling."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector_happy_path(self, mock_post: Mock) -> None:
        """Happy path should return dominant emotion and scores."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.02,
                        "fear": 0.03,
                        "joy": 0.92,
                        "sadness": 0.02,
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am very glad this happened")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["anger"], 0.01)
        self.assertEqual(result["disgust"], 0.02)
        self.assertEqual(result["fear"], 0.03)
        self.assertEqual(result["joy"], 0.92)
        self.assertEqual(result["sadness"], 0.02)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector_empty_text_returns_none(self, mock_post: Mock) -> None:
        """Status 400 should return None values for all keys."""
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        result = emotion_detector("")

        self.assertEqual(
            result,
            {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            },
        )


if __name__ == "__main__":
    unittest.main()
