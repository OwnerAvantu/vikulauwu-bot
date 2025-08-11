# main.py — самый простой сервер, чтобы получить домен
import os
from fastapi import FastAPI, Request, Header

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/lava/webhook")
async def lava_webhook(request: Request, x_signature: str | None = Header(default=None)):
    # пока просто принимаем вебхук и пишем в логи
    body = await request.body()
    print("LAVA WEBHOOK:", body[:500])
    return {"ok": True}

@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    print("TG UPDATE:", str(data)[:500])
    return {"ok": True}
