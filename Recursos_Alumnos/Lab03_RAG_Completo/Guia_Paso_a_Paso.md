# Lab 3: Pipeline RAG Corporativo con ChromaDB 🧠

## Objetivo
Implementar un buscador semántico. El script tomará documentos de texto, los fragmentará (Chunking), los convertirá a vectores y los guardará en ChromaDB. Luego, haremos preguntas que solo puedan ser respondidas usando la base vectorial.

## Instrucciones
1. Instalar dependencias: `pip install langchain langchain-openai chromadb tiktoken`
2. El archivo `rag_pipeline.py` contiene la lógica de ingesta y recuperación.
3. Modifica los textos de ejemplo con información ficticia de tu empresa (ej. Políticas de vacaciones).
4. Ejecuta el script y evalúa si la IA responde basándose SOLO en el contexto.
