# [START scc_slack_notification]
import base64
import json
import requests
import functions_framework

# In production, prefer using environment variables or Secret Manager
# to store sensitive information like tokens.
TOKEN = "YOUR_BOT_ACCESS_TOKEN"

@functions_framework.cloud_event
def send_slack_chat_notification(cloud_event):
    pubsub_message = base64.b64decode(cloud_event.data["message"]["data"]).decode('utf-8').strip()
    message_json = json.loads(pubsub_message)

    finding = message_json['finding']

    requests.post("https://slack.com/api/chat.postMessage", data={
        "token": TOKEN,
        "channel": "#YOUR_SLACK_CHANNEL_NAME",
        "text": f"A high severity finding {finding['category']} was detected."
    })
# [END scc_slack_notification]
