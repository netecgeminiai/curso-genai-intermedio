# Guía de Preparación de Entorno (Setup) 🛠️

Para realizar las prácticas del curso **IA Generativa Intermediate (70% Práctico)**, requieres configurar tu entorno local.

## 1. Requisitos Previos
* Python 3.10 o superior instalado.
* Visual Studio Code (o tu IDE preferido).
* Una API Key de OpenAI y/o Google Gemini.

## 2. Creación del Entorno Virtual (VENV)
Abre tu terminal en la carpeta de tus laboratorios y ejecuta:
```bash
python -m venv venv

# Activar en Windows:
venv\Scripts\activate
# Activar en Mac/Linux:
source venv/bin/activate
```

## 3. Instalación de Dependencias Base
Para la mayoría de los laboratorios usaremos estas librerías:
```bash
pip install openai google-generativeai fastapi uvicorn pydantic langchain langchain-openai chromadb
```

## 4. Configuración de Variables de Entorno
Nunca pongas tus API Keys directo en el código. Crea un archivo llamado `.env` en la raíz de tu proyecto:
```env
OPENAI_API_KEY=sk-tu-api-key-aqui
GEMINI_API_KEY=AIza-tu-api-key-aqui
```
En Python, lo cargaremos usando `python-dotenv`. ¡Estás listo para iniciar los laboratorios!
