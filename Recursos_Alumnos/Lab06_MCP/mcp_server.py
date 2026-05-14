from mcp.server.fastmcp import FastMCP
from datetime import datetime

# Instanciar el servidor MCP
mcp = FastMCP("ServidorHoraLocal")

@mcp.tool()
def obtener_hora_actual() -> str:
    """
    Obtiene la hora actual del sistema en formato de texto.
    Útil cuando el usuario pregunta 'qué hora es'.
    """
    ahora = datetime.now()
    return f"La hora local del servidor es: {ahora.strftime('%H:%M:%S')}"

if __name__ == "__main__":
    print("Iniciando Servidor MCP...")
    # Corre sobre stdio (Standard Input/Output), el protocolo por defecto para herramientas locales
    mcp.run()
