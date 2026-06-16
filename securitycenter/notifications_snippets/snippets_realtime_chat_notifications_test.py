import base64
import json
from unittest import mock
import pytest
import snippets_realtime_chat_notifications

def test_send_slack_chat_notification():
    # Mock the requests.post call
    with mock.patch("snippets_realtime_chat_notifications.requests.post") as mock_post:
        # Simulate a Pub/Sub event
        finding_data = {"finding": {"category": "test-category"}}
        event_data = {
            "message": {
                "data": base64.b64encode(json.dumps(finding_data).encode('utf-8')).decode('utf-8')
            }
        }
        mock_event = mock.Mock()
        mock_event.data = event_data

        snippets_realtime_chat_notifications.send_slack_chat_notification(mock_event)

        # Assert requests.post was called with expected arguments
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        assert args[0] == "https://slack.com/api/chat.postMessage"
        assert kwargs['data']['text'] == "A high severity finding test-category was detected."
