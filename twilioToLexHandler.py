import json
import boto3
import base64
import urllib.parse

# Initialize the Lex client
lex_client = boto3.client("lexv2-runtime")

# Replace with your actual Lex bot info
BOT_ID = "SSNWBHD5F5"            # Your Lex V2 Bot ID
BOT_ALIAS_ID = "TSTALIASID"      # Your Bot Alias ID
BOT_LOCALE = "en_US"             # Locale ID

def lambda_handler(event, context):
    print("=== RAW EVENT ===")
    print(json.dumps(event))

    try:
        # Decode base64-encoded body if necessary
        body = event.get("body", "")
        if event.get("isBase64Encoded", False):
            body = base64.b64decode(body).decode("utf-8")

        print("📦 Raw form-encoded body:", body)

        # Parse form data
        form_data = urllib.parse.parse_qs(body)
        print("💬 Decoded form:", form_data)

        from_number = form_data.get('From', ['unknown'])[0]
        body_text = form_data.get('Body', [''])[0]

        # Clean session ID for Lex (must match regex [0-9a-zA-Z._:-]+)
        clean_number = from_number.replace("whatsapp:", "").replace("+", "").replace(" ", "")
        session_id = f"whatsapp_{clean_number}"

        print(f"💬 Received from {clean_number} → {body_text}")

        # Send user input to Lex
        lex_response = lex_client.recognize_text(
            botId=BOT_ID,
            botAliasId=BOT_ALIAS_ID,
            localeId=BOT_LOCALE,
            sessionId=session_id,
            text=body_text
        )

        # Extract Lex message
        lex_message = "🤖 Sorry, no reply from Lex."
        messages = lex_response.get("messages", [])
        if messages:
            lex_message = messages[0].get("content", lex_message)

        print("🧠 Lex response:", lex_message)

        # Return response to Twilio
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/xml"
            },
            "body": f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{lex_message}</Message>
</Response>"""
        }

    except Exception as e:
        print("❌ Error occurred:", str(e))
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/xml"
            },
            "body": f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>⚠️ Error while processing your message.</Message>
</Response>"""
        }
