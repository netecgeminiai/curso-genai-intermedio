from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI(title="GenAI Model Router")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class UserRequest(BaseModel):
    prompt: str

def call_cheap_model(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def call_expensive_model(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

@app.post("/chat")
async def router(request: UserRequest):
    word_count = len(request.prompt.split())
    
    if word_count > 20:
        respuesta_ia = call_expensive_model(request.prompt)
        modelo_usado = "gpt-4o (Costoso)"
    else:
        respuesta_ia = call_cheap_model(request.prompt)
        modelo_usado = "gpt-4o-mini (Económico)"
        
    return {
        "modelo_enrutado": modelo_usado,
        "response": respuesta_ia
    }
