import requests #libreria para pedirle a python

respuesta = requests.get("http://127.0.0.1:8000")

print(respuesta) 
print(respuesta.raw) #direccion en memoria
print(respuesta.text) #respuesta en texto
print(respuesta.json()) #respuesta en diccionario

diccionario=respuesta.json()
print(diccionario["Hola"])


def peticion_path_id():
    respuesta = requests.get("http://127.0.0.1:8000/path/1")
    print(respuesta.json())
    
peticion_path_id()

def peticion_multiples_path_id_nombre_edad():
    respuesta=requests.get("http://127.0.0.1:8000/multiples/path/2/Edwin/25")
    print(respuesta.json())
    
peticion_multiples_path_id_nombre_edad()
    
    #activar uvicorn 
    #estar en la carpeta del archivo
    #uvicorn main2:app --reload