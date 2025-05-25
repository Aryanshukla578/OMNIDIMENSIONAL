from fastapi import FastAPI, Request
from utils.fetch_deals import search_deals
from utils.voice_agent import start_call_agent
from utils.logger import log_to_sheets
from utils.seller_call_flow import handle_seller_conversation

app = FastAPI()

@app.post("/endpoint")
async def assistant(request: Request):
    data = await request.json()
    product = data.get("product")
    link = data.get("link", None)
    deals = search_deals(product, link)
    top_deals = sorted(deals, key=lambda x: x['price'])[:3]
    for deal in top_deals:
        handle_seller_conversation(deal)
        log_to_sheets(deal)
    return {"top_deals": top_deals}
