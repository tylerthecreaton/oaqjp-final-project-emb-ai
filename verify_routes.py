"""Quick route checks for assignment verification."""

from server import app

client = app.test_client()

root = client.get("/")
print("ROOT_STATUS", root.status_code)

blank = client.get("/emotionDetector?textToAnalyze=")
print("BLANK_STATUS", blank.status_code)
print("BLANK_BODY", blank.get_data(as_text=True))
