import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# 1. Datos falsos empresariales
documentos_corporativos = [
    "La política de vacaciones 2026 indica que los empleados tienen 20 días libres.",
    "El presupuesto para equipo de oficina remoto es de $500 USD por empleado.",
    "Las credenciales de AWS no deben enviarse por Slack, usar AWS Secrets Manager."
]

# 2. Chunking (Fragmentación)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
docs = text_splitter.create_documents(documentos_corporativos)

# 3. Vectorización e Ingesta en ChromaDB (Base de Datos Local)
vectorstore = Chroma.from_documents(documents=docs, embedding=OpenAIEmbeddings())

# 4. Recuperador (Retriever)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 5. Prompt Restrictivo
template = """
Responde a la pregunta basándote ÚNICAMENTE en el siguiente contexto.
Si la respuesta no está en el contexto, di "No tengo información oficial al respecto".

Contexto: {context}

Pregunta: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# 6. Cadena LCEL (LangChain Expression Language)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# Ejecución
pregunta = "¿Cuánto dinero me dan para armar mi oficina en casa?"
print(f"Pregunta: {pregunta}")
respuesta = rag_chain.invoke(pregunta)
print(f"Respuesta IA: {respuesta.content}")
