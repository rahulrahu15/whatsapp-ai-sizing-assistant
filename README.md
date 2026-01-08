# WhatsApp SizeAdvisor Bot 🧠📱

A serverless AI-powered chatbot built using **Amazon Lex V2**, **AWS Lambda**, **DynamoDB**, **API Gateway**, and **Twilio**. This bot collects user body measurements over WhatsApp and provides personalized clothing size recommendations.

---

## 🚀 Features

- ✅ Collects user inputs: **Height**, **Weight**, **Fit Preference**, and **Usual Size**
- ✅ Integrates with **WhatsApp** via **Twilio**
- ✅ Uses **Amazon Lex V2** for natural language understanding
- ✅ Persists user data to **DynamoDB**
- ✅ Deployed via **AWS Lambda** + **API Gateway**
- ✅ End-to-end serverless infrastructure

---

🛠️ Setup Instructions
1. 🧠 Create Lex V2 Bot
Intent: CollectSizeDetails

Slots: Height, Weight, FitPreference, UsualSize

Enable Lambda code hooks for dialog and fulfillment

2. ⚙️ Create Lambda Function (SizeAdvisorHandler)
Write logic to extract slot values and store in DynamoDB

Attach IAM policy for DynamoDB write access

3. 🧱 Create DynamoDB Table
Table Name: SizeAdvisorUserData

Primary Key: userId (String)

4. 🌐 Create API Gateway
Resource path: /twilioToLexHandler

Integration type: Lambda Proxy Integration

Method: ANY

5. 🔗 Configure Twilio
Phone Number: Enable for WhatsApp Sandbox

Webhook URL: Set to your API Gateway endpoint

🧪 Sample Conversation
text
Copy
Edit
User: I want a size recommendation
Bot: What is your height in centimeters?
User: 170
Bot: Great! What is your weight in kilograms?
User: 70
Bot: How do you prefer the fit? (slim, regular, loose)
User: Slim
Bot: What size do you usually wear? (S, M, L, etc.)
User: M
Bot: ✅ We've saved your preferences: 170 cm, 70 kg, slim fit, size M.

Folder Structure
.
├── lambda/
│   ├── twilioToLexHandler.py
│   └── sizeAdvisorHandler.py
├── README.md
└── architecture.png



