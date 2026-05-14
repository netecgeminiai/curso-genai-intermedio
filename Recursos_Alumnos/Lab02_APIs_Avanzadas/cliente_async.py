import asyncio
import os
from openai import AsyncOpenAI
from pydantic import BaseModel
from tenacity import retry, wait_exponential, stop_after_attempt

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Forzar el Output a JSON Estructurado
class AnalisisSentimiento(BaseModel):
    sentimiento: str
    score: int
    motivo_principal: str

# Decorador para reintentar si OpenAI devuelve HTTP 429 (Rate Limit)
@retry(wait=wait_exponential(multiplier=1, min=2, max=10), stop=stop_after_attempt(3))
async def analizar_resena(resena: str):
    response = await client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Analiza la siguiente reseña de usuario."},
            {"role": "user", "content": resena}
        ],
        response_format=AnalisisSentimiento
    )
    return response.choices[0].message.parsed

async def main():
    resenas = [
        "La app es súper lenta y se traba a cada rato.",
        "Me encantó el nuevo diseño, muy intuitivo.",
        "El servicio al cliente nunca responde mis correos."
    ]
    
    # Ejecución concurrente
    tareas = [analizar_resena(r) for r in resenas]
    resultados = await asyncio.gather(*tareas)
    
    for r in resultados:
        print(f"Sentimiento: {r.sentimiento} ({r.score}/10) -> {r.motivo_principal}")

if __name__ == "__main__":
    asyncio.run(main())
