# Lab 1: Enrutador de Modelos GenAI con FastAPI 🚦

## Objetivo
Implementar una API en FastAPI que evalúe la complejidad de un prompt entrante y decida si debe enviarlo a un modelo barato (gpt-4o-mini) o a un modelo de alto razonamiento (gpt-4o), optimizando costos en producción.

## Paso a Paso

### Paso 1: Estructura Básica
Crea el archivo `router_api.py`. Importa FastAPI y Pydantic para definir el esquema de datos que el usuario nos enviará por POST.

### Paso 2: Lógica de Enrutamiento
Crea una función `route_model(prompt)`. 
* **Regla de negocio:** Si el texto tiene menos de 20 palabras, asumimos que es una tarea sencilla de NLP.
* Si tiene más, requiere contexto profundo.

### Paso 3: Integración de OpenAI
Instancia el cliente de OpenAI. Configura las llamadas correspondientes en cada rama del `if/else`.

### Paso 4: Ejecución
Ejecuta el servidor localmente con Uvicorn:
```bash
uvicorn router_api:app --reload
```
Abre Postman o Swagger (`http://localhost:8000/docs`) y prueba enviando un prompt corto y uno largo.
