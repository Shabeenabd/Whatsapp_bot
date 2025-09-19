from fastapi import FastAPI, Request
# from twilio

app = FastAPI()

@app.get("/")
async def read_root(request : Request):
    query_params = dict(request.query_params)
    headers = dict(request.headers)
    client_host = request.client.host
    return {
        "method": request.method,
        "url": str(request.url),
        "client_ip": client_host,
    }


@app.post("/webhook")
async def web_hook(name: str):
    return f"Hello {name}"
