from fastapi import FastAPI, Request
from twilio.twiml.messaging_response import MessagingResponse
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/whatsapp")
async def whatsapp_reply(Body: str = None):
    # incoming_msg = Body.lower()
    resp = MessagingResponse()
    msg = resp.message()
    msg.body("Hi 👋! I’m your AI assistant. How can I help you today?")
    # if  'hi' in incoming_msg:
    #     msg.body("Hi 👋! I’m your AI assistant. How can I help you today?")
    # else:
    #     msg.body(f"You said: {Body} \n i say good!!!!!!!")
    
    reply = PlainTextResponse(str(resp)) 
    return reply


@app.get("/")
async def read_root(request : Request):
    client_host = request.client.host
    return {
        "method": request.method,
        "url": str(request.url),
        "client_ip": client_host,
    }
