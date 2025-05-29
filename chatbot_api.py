from fastapi import FastAPI
from pydantic import BaseModel
from model import ChatbotModel

# Inicializa FastAPI
app = FastAPI()
chatbot = ChatbotModel()

# Esquema del mensaje que se recibe por POST
class Mensaje(BaseModel):
    texto: str

@app.get("/")
def leer_raiz():
    return {"mensaje": "API del Chatbot funcionando correctamente 🎉"}

@app.post("/chat")
def responder_mensaje(mensaje: Mensaje):
    respuesta = chatbot.responder(mensaje.texto)
    # Aseguramos que la respuesta sea una cadena (por si viene en tupla)
    if isinstance(respuesta, tuple):
        respuesta = " ".join(respuesta)
    return {"respuesta": respuesta}
