from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Servidor funcionando"}

# RUTA SOLICITADA EN LA TAREA 0
@app.get("/tarea-0")
def tarea_cero():
    return {"respuesta": "Primer tarea realizada"}
