#Librerias
import json
from rapidfuzz import process
import random
import os
"""
#Mensajes de bienvenida y despedida
nombre = input("Hola, ¿Cómo te llamas? ")
print(f"Muchos gusto, {nombre}. Soy un chatbot de memoria 😊")
print("Escribe Salir para terminar la conversación.")"""

class ChatbotModel:
    def __init__(self):

        #Diccionario con reglas
        #Carga respuestas desde un archivo JSON
        ruta = os.path.join(os.path.dirname(__file__), 'respuestas.json')
        with open(ruta, 'r', encoding='utf-16') as f:
            self.respuestas = json.load(f)    
        
        # Función para encontrar la mejor coincidencia
        self.frases_conocidas = list(self.respuestas.keys())
        self.preguntas_previas = set()

    def responder(self, mensaje_usuario):
        mensaje_usuario = mensaje_usuario.upper().strip()# convertimos a minúsculas para facilitar la comparación

        if mensaje_usuario == "salir":
            return "Conversación finalizada"
        
        # Buscamos la mejor coincidencia con fuzzy matching
        mejor, score, _ = process.extractOne(mensaje_usuario, self.frases_conocidas)

        if score >= 80: #Puedes ajustar ese valor
            if mejor in self.preguntas_previas:
                respuesta = random.choice(self.respuestas[mejor])
                print("Ya me habías preguntado eso pero igual te respondo", respuesta)
                return "Ya me habías preguntado eso pero igual te respondo", respuesta
            self.preguntas_previas.add(mejor)    
            respuesta = random.choice(self.respuestas[mejor])
            print(respuesta)
            return respuesta
        else:
            print("Lo siento, no entiendo esa pregunta.")
            return("Lo siento, no entiendo esa pregunta.")
# Fin del código

"""Validar información extrada del documento ya que lee línea por línea y no por párrafos"""