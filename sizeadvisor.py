import json
import boto3
import uuid
from datetime import datetime

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SizeAdvisorUserData')  # Make sure this matches your actual table name

def lambda_handler(event, context):
    print("=== Full Lex Event ===")
    print(json.dumps(event, indent=4))

    # Use session ID or generate one
    session_id = event.get("sessionId", str(uuid.uuid4()))

    # Extract slots safely
    slots = event.get("sessionState", {}).get("intent", {}).get("slots", {})

    def get_slot_value(slot_name):
        return slots.get(slot_name, {}).get("value", {}).get("interpretedValue", "unknown")

    height = get_slot_value("Height")
    weight = get_slot_value("Weight")
    fit = get_slot_value("FitPreference")
    size = get_slot_value("UsualSize")

    print(f"✅ Extracted values: Height={height}, Weight={weight}, Fit={fit}, Size={size}")

    # Prepare DynamoDB item
    item = {
        "userId": session_id,
        "height": height,
        "weight": weight,
        "fitPreference": fit,
        "usualSize": size,
        "timestamp": str(datetime.utcnow())
    }

    # Store to DynamoDB
    try:
        table.put_item(Item=item)
        print("✅ Data stored in DynamoDB:", item)
    except Exception as e:
        print("❌ Error storing to DynamoDB:", str(e))

    # Lex response
    return {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "name": event["sessionState"]["intent"]["name"],
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": f"Thanks! We've saved your preferences: {height} cm, {weight} kg, {fit} fit, size {size}."
            }
        ]
    }
