from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from dotenv import load_dotenv
import os
import time
import re

load_dotenv()

with open("prompt.txt", "r") as f:
    SYSTEM_PROMPT = f.read()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def sanitize(text: str) -> str:
    text = re.sub(r"[<>]", "", text)
    return text.strip()[:500]

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = sanitize(data.get("message", ""))
    history = data.get("history", [])
    if not isinstance(history, list):
        history = []

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in history[-10:]:
        if "role" in msg and "content" in msg:
            messages.append({
                "role": msg["role"],
                "content": msg["content"][:1000]
            })
    messages.append({"role": "user", "content": message})

    try:
        start = time.time()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=180,
            timeout=15
        )
        duration = int((time.time() - start) * 1000)
        reply = response.choices[0].message.content
        return {"reply": reply, "duration_ms": duration}

    except Exception as e:
        print("Chat error:", e)
        return {"reply": "I can't answer right now. Please message me on WhatsApp: +1 305-218-3772"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"api": "Luis CV chatbot", "status": "running"}