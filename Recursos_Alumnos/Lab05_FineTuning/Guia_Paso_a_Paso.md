# Lab 5: Preparación de Datos para Fine-Tuning 🧠

## Objetivo
Convertir un dataset en bruto (CSV) a formato estructurado `JSONL` requerido por la API de OpenAI para realizar el Fine-Tuning de un modelo GPT.

## Paso a Paso

### Paso 1: Dependencias
Asegúrate de instalar pandas:
```bash
pip install pandas
```

### Paso 2: Script de Conversión
Crea el archivo `csv_to_jsonl.py`. Usaremos Pandas para leer un archivo CSV hipotético `soporte.csv` que tiene columnas "pregunta" y "respuesta".

### Paso 3: Lógica
Iteramos el DataFrame. Por cada fila, creamos el diccionario de roles: system, user (pregunta) y assistant (respuesta).

### Paso 4: Exportación
Guardamos en formato `.jsonl`.
