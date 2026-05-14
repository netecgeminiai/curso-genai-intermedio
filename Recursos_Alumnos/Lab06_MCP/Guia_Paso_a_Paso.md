# Lab 6: Servidor Model Context Protocol (MCP) 🔌

## Objetivo
Crear un servidor local MCP en Python que exponga una herramienta segura para que un agente autónomo (como Claude o Cursor) pueda leer la hora actual del sistema.

## Paso a Paso

### Paso 1: Instalación del SDK
```bash
pip install mcp
```

### Paso 2: Creación del Servidor
Crea el archivo `mcp_server.py`. Importa FastMCP del SDK.

### Paso 3: Registro de Herramientas
Crea una función en Python para leer la hora y decórala con `@mcp.tool()`. Agrega docstrings detallados, el LLM los usará para entender qué hace.

### Paso 4: Ejecución
Inicia el servidor.
