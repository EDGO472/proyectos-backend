from fastapi import FastAPI

app = FastAPI()  
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
