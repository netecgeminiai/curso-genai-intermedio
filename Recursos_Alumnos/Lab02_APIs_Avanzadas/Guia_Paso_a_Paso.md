# Lab 2 Avanzado: Llamadas Asíncronas y Pydantic ⚡

## Objetivo
En producción, no podemos bloquear el hilo principal de Python esperando a la IA. Debemos usar llamadas asíncronas (`asyncio`). Además, forzaremos a la IA a devolver un esquema de datos estructurado perfecto usando `Pydantic` y manejaremos caídas por Rate Limits con `Tenacity`.

## Instrucciones
1. Revisa el archivo `cliente_async.py`.
2. Instala dependencias: `pip install openai pydantic tenacity asyncio`
3. Analiza cómo la clase `AnalisisSentimiento` fuerza la salida del modelo.
4. Ejecuta el código con una lista de 5 reseñas de clientes y observa cómo se procesan de forma concurrente sin bloquearse, superando las validaciones de JSON.
