# Servidor de Tareas MCP

## Descripción

Este proyecto consiste en la implementación de un servidor básico utilizando Model Context Protocol (MCP) y Python.

El servidor permite administrar una lista de tareas almacenadas localmente en un archivo JSON. Se implementaron Resources, Tools y Prompts para demostrar el funcionamiento básico de MCP.

## Funcionalidades

El servidor cuenta con las siguientes funcionalidades:

### Resource

`tasks://all`

Permite consultar todas las tareas almacenadas en el archivo `tasks.json`.

### Tools

#### add_task

Permite agregar una nueva tarea indicando:

- Nombre
- Descripción
- Prioridad

Las prioridades permitidas son:

- alta
- media
- baja

#### complete_task

Permite marcar una tarea como completada utilizando su ID.

### Prompt

#### daily_summary

Genera una plantilla con un resumen diario que incluye:

- Total de tareas
- Tareas completadas
- Tareas pendientes
- Lista de tareas pendientes
- Prioridad de cada tarea

## Estructura del proyecto

mcp-todo-server/

- server.py
- tasks.json
- requirements.txt
- README.md

## Requisitos

Para ejecutar el proyecto se necesita:

- Python
- uv
- FastMCP
- MCP Inspector

## Instalación

Crear el entorno virtual:

    uv venv

Instalar las dependencias:

    uv pip install -r requirements.txt

Instalar FastMCP:

    uv pip install fastmcp

## Ejecución

Para iniciar el servidor:

    uv run python server.py

El servidor utiliza el transporte `stdio`.

## Pruebas con MCP Inspector

Para iniciar MCP Inspector:

    npx @modelcontextprotocol/inspector uv run python server.py

Desde MCP Inspector se pueden probar los Resources, Tools y Prompts del servidor.

## Interacciones realizadas

### Prueba 1 - Consultar tareas

Se utilizó el Resource `tasks://all` para obtener las tareas almacenadas en `tasks.json`.

Resultado: el servidor mostró correctamente las tareas existentes.

### Prueba 2 - Agregar una tarea

Se utilizó la herramienta `add_task` con los siguientes datos:

Nombre: Preparar exposición

Descripción: Estudiar el funcionamiento del servidor MCP

Prioridad: alta

Resultado: la tarea fue agregada correctamente con el ID 3.

### Prueba 3 - Completar una tarea

Se utilizó la herramienta `complete_task` con el ID 3.

Resultado: la tarea "Preparar exposición" fue marcada como completada.

### Prueba 4 - Resumen diario

Se ejecutó el Prompt `daily_summary`.

Resultado:

- Total de tareas: 3
- Tareas completadas: 1
- Tareas pendientes: 2

El Prompt identificó correctamente las tareas pendientes y sus prioridades.

## Tecnologías utilizadas

- Python
- Model Context Protocol (MCP)
- FastMCP
- JSON
- MCP Inspector

## Conclusión

La implementación permitió comprender de forma práctica el funcionamiento de Model Context Protocol. Mediante un servidor MCP se logró exponer información utilizando Resources, ejecutar acciones mediante Tools y generar plantillas reutilizables mediante Prompts.

El uso de MCP facilita la comunicación entre aplicaciones de inteligencia artificial y diferentes herramientas o fuentes de datos utilizando una estructura estandarizada.