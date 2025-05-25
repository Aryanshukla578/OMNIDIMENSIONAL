# 🧠 OmniDimensional AI Assistant

A powerful voice-enabled AI agent that helps users find the best deals on high-demand products (e.g., sneakers, concert tickets) by calling sellers, gathering real-time data, negotiating prices, and sending summaries via email.

![Voice Assistant Process Flowchart](assets/voice_assistant_flowchart.png)

---

## 🔗 Referenced Repositories

- Integrated with **Pathway** as a dynamic knowledge base:  
  [https://github.com/pathwaycom/llm-app.git](https://github.com/pathwaycom/llm-app.git)

---

## 🚀 Features

- 🎙️ Voice-powered negotiation with sellers using OmniDimension  
- 🔍 Real-time price comparison and product availability check  
- 🧠 Retrieval-Augmented Generation (RAG) via OpenAI / LangChain / LlamaIndex  
- 🔄 Dynamic Knowledge Updates using Pathway  
- 🧾 Google Sheets logging via webhook for call and deal data  
- 📧 Email summaries sent via Gmail API or SendGrid  
- 🧩 Modular FastAPI backend for seamless integration  

![Feature Diagram](https://via.placeholder.com/800x400.png?text=Features+Diagram)

---

## 📁 Folder Structure



OmniDimensional_AI_Agent/
├── main.py # FastAPI app entrypoint
├── requirements.txt # All Python dependencies
├── config.yaml # API keys, platforms, and settings
├── README.md # This file
│
├── utils/
│ ├── fetch_deals.py # Fetch data from Amazon, Flipkart, StockX
│ ├── voice_agent.py # Voice interface using OmniDimension
│ ├── seller_call_flow.py # Call script, negotiation steps
│ └── logger.py # Logs interactions to Google Sheets
│
├── templates/
│ └── email_template.html # HTML email summary
│
└── data/
└── example_product_requests.json # Sample input JSON

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/OmniDimensional_AI_Agent.git
   cd OmniDimensional_AI_Agent
2.  Install Dependencies
 pip install -r requirements.txt
3.Configure

Update config.yaml with:

Google Sheets Webhook

Gmail or SendGrid API keys

Platform settings (Amazon, Flipkart, etc.)
4.Run the server
uvicorn main:app --reload
🧠 Voice Interaction Flow
AI initiates call → Identifies seller

Introduces purpose → Asks for product, price, and delivery

Negotiates price if possible

Logs all interaction data

Sends top 3 deals to user via email
Subject: Best Sneaker Deals Just For You

Hi there,

Here are the top 3 deals on Air Jordan 4 Retro:

1. Nike.com - Rs. 18,999 - Ships in 2 days
2. Flipkart - Rs. 17,499 - Ships in 5 days
3. StockX - Rs. 19,200 - Ships in 3 days

Click here to view full details and place your order.

Best,  
AI Deal Assistant
🔐 Security
API keys and email credentials should be stored securely using .env or secrets manager

Ensure your webhook URL is protected and authenticated

🛠 Future Improvements
Add product review analysis

Add SMS/WhatsApp notification option

Multilingual voice support

📄 License
This project is licensed under MIT. Reference Pathway's original llm-app repo for further extensions.

🤝 Contributing
PRs welcome. For major changes, open an issue first to discuss what you’d like to change or improve.


Let me know if you want this dropped into your project folder and zipped for download again.
