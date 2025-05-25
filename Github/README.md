# OmniDimensional AI Assistant

This project builds an omnidimensional AI voice agent capable of:
- Searching deals in real-time
- Contacting sellers and negotiating
- Logging results to Google Sheets
- Emailing top options to the user

### Powered by:
- **FastAPI** for the API layer
- **Pathway** for real-time knowledge tracking and streaming pipelines
- **LangChain / OpenAI** for conversational context
- **Google Sheets API** for structured logging
- **SendGrid** for email updates

### Setup Instructions:
1. Clone the repo
```bash
git clone https://github.com/pathwaycom/llm-app.git
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the API
```bash
uvicorn main:app --reload
```
