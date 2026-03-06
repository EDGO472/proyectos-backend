import requests

# Esta es tu URL real de Render
url = "https://proyectos-backend-lx4q.onrender.com"

try:
    response = requests.get(url)
    print("Respuesta de la API:")
    print(response.json())
except Exception as e:
    print(f"Error al conectar con Render: {e}")
