"""Script to demonstrate formatted output from emotion_detector."""

from EmotionDetection import emotion_detector

print("=" * 70)
print("EMOTION DETECTION - FORMATTED OUTPUT TEST")
print("=" * 70)

print("\nTest 1: Testing emotion_detector function output format")
print("-" * 70)
result = emotion_detector("I am glad this happened")
print(f"Result: {result}")

print("\n\nTest 2: Formatted Output Structure")
print("-" * 70)
print(f"Anger:            {result['anger']}")
print(f"Disgust:          {result['disgust']}")
print(f"Fear:             {result['fear']}")
print(f"Joy:              {result['joy']}")
print(f"Sadness:          {result['sadness']}")
print(f"Dominant Emotion: {result['dominant_emotion']}")

print("\n" + "=" * 70)
print("Output format verification: PASSED")
print("Function returns dictionary with all required keys")
print("=" * 70)
