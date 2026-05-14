import pandas as pd
import json

# Simulación de lectura de datos
# df = pd.read_csv("soporte.csv")
data = [
    {"pregunta": "Cómo reseteo mi password?", "respuesta": "Ve a ajustes > Seguridad > Reset."},
    {"pregunta": "El sistema está lento", "respuesta": "Por favor, borra la caché de tu navegador e intenta de nuevo."}
]
df = pd.DataFrame(data)

jsonl_path = "dataset_entrenamiento.jsonl"
system_prompt = "Eres un asistente de soporte técnico amable y directo."

with open(jsonl_path, 'w', encoding='utf-8') as f:
    for _, row in df.iterrows():
        conversacion = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": row["pregunta"]},
                {"role": "assistant", "content": row["respuesta"]}
            ]
        }
        f.write(json.dumps(conversacion, ensure_ascii=False) + '\n')

print(f"Dataset guardado en {jsonl_path}")
