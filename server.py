import json
from pathlib import Path

from fastmcp import FastMCP


# Crear el servidor MCP
mcp = FastMCP("Servidor de Tareas MCP")

# Ubicación del archivo tasks.json
TASKS_FILE = Path(__file__).parent / "tasks.json"


def cargar_tareas():
    """Lee las tareas almacenadas en tasks.json."""
    if not TASKS_FILE.exists():
        return []

    with open(TASKS_FILE, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_tareas(tareas):
    """Guarda las tareas en tasks.json."""
    with open(TASKS_FILE, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)


# =========================================================
# RESOURCE: CONSULTAR TAREAS
# =========================================================

@mcp.resource("tasks://all")
def obtener_tareas() -> str:
    """Retorna la lista de tareas almacenadas."""
    tareas = cargar_tareas()

    return json.dumps(
        tareas,
        indent=4,
        ensure_ascii=False
    )


# =========================================================
# TOOL 1: AGREGAR TAREA
# =========================================================

@mcp.tool()
def add_task(
    nombre: str,
    descripcion: str,
    prioridad: str
) -> str:
    """
    Agrega una nueva tarea.
    La prioridad debe ser alta, media o baja.
    """

    prioridad = prioridad.lower()

    if prioridad not in ["alta", "media", "baja"]:
        return "Error: la prioridad debe ser alta, media o baja."

    tareas = cargar_tareas()

    if tareas:
        nuevo_id = max(tarea["id"] for tarea in tareas) + 1
    else:
        nuevo_id = 1

    nueva_tarea = {
        "id": nuevo_id,
        "nombre": nombre,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "completada": False
    }

    tareas.append(nueva_tarea)
    guardar_tareas(tareas)

    return (
        f"Tarea agregada correctamente. "
        f"ID: {nuevo_id}, "
        f"Nombre: {nombre}, "
        f"Prioridad: {prioridad}"
    )


# =========================================================
# TOOL 2: COMPLETAR TAREA
# =========================================================

@mcp.tool()
def complete_task(id: int) -> str:
    """Marca una tarea como completada utilizando su ID."""

    tareas = cargar_tareas()

    for tarea in tareas:
        if tarea["id"] == id:

            if tarea["completada"]:
                return f"La tarea con ID {id} ya estaba completada."

            tarea["completada"] = True
            guardar_tareas(tareas)

            return (
                f"Tarea '{tarea['nombre']}' "
                f"marcada como completada."
            )

    return f"No existe una tarea con el ID {id}."


# =========================================================
# PROMPT: RESUMEN DIARIO
# =========================================================

@mcp.prompt()
def daily_summary() -> str:
    """Genera una plantilla con el estado actual de las tareas."""

    tareas = cargar_tareas()

    total = len(tareas)

    completadas = sum(
        1 for tarea in tareas
        if tarea["completada"]
    )

    pendientes = total - completadas

    tareas_pendientes = [
        tarea
        for tarea in tareas
        if not tarea["completada"]
    ]

    texto_pendientes = "\n".join(
        f"- {tarea['nombre']} "
        f"(Prioridad: {tarea['prioridad']})"
        for tarea in tareas_pendientes
    )

    if not texto_pendientes:
        texto_pendientes = "No existen tareas pendientes."

    return f"""
Genera un resumen diario del estado actual de las tareas.

Total de tareas: {total}
Tareas completadas: {completadas}
Tareas pendientes: {pendientes}

Tareas pendientes:
{texto_pendientes}

Presenta el resumen de forma clara, breve y ordenada.
"""


# =========================================================
# INICIAR SERVIDOR
# =========================================================

if __name__ == "__main__":
    mcp.run()