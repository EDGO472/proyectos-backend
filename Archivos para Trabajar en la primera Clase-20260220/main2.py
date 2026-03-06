from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()  

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    en_stock: bool = True  # Valor por defecto


    #parametros
@app.get("/")    #funcion decoradora(resive una funcion)
def prueba():
    return {"Hola":"Mundo"}  

@app.get("/path/{id}")
def path_wraper(id:int):
    return{"Usuario":id}

@app.get("/multiples/path/{id}/{nombre}/{edad}")
def multiples_path_wraper(id:int, nombre:str, edad:int):
    return{"Usuario":id,"nombre":nombre,"edad":edad}

@app.post("/productos/")
def crear_producto(producto: Producto):
    return {"mensaje": "Producto guardado", "data": producto}

# Importa Optional desde typing (agrégalo al inicio de tu archivo)
from typing import Optional

# ... (tus clases y funciones anteriores se quedan igual)

@app.get("/items/")
def leer_items(nombre: str, precio: float, impuesto: Optional[float] = None):
    # 'nombre' y 'precio' son obligatorios.
    # 'impuesto' es OPCIONAL (si no lo mandan, vale None).
    
    resultado = {"item_nombre": nombre, "item_precio": precio}
    
    if impuesto:
        resultado.update({"precio_total": precio + impuesto})
        
    return resultado
