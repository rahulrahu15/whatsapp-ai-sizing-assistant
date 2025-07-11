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

## 📷 Architecture

```mermaid
graph TD
    A[User via WhatsApp] -->|Sends Message| B[Twilio Webhook]
    B -->|POST| C[API Gateway Endpoint]
    C --> D[AWS Lambda (twilioToLexHandler)]
    D --> E[Amazon Lex V2 Bot]
    E --> F[Lambda Fulfillment Function]
    F --> G[DynamoDB (User Data)]
    F -->|Response| E
    E -->|Final Reply| A
