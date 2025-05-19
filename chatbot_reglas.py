#Librerias
from rapidfuzz import process
import random

#Mensajes de bienvenida y despedida
nombre = input("Hola, ¿Cómo te llamas? ")
print(f"Muchos gusto, {nombre}. Soy un chatbot de memoria 😊")
print("Escribe Salir para terminar la conversación.")

#Diccionario con reglas
respuestas = {
    "hola": [
        "¡Hola! ¿Cómo estás?",
        "¡Hey! Qué gusto verte.",
        "Hola, ¿en qué puedo ayudarte?"
    ],
    "¿cómo estás?": [
        "Estoy bien, gracias por preguntar 😊",
        "Todo bien por aquí, ¿y tú?",
        "¡Excelente! ¿Cómo estás tú?"
    ],
    "como estas": [
        "Estoy bien, gracias por preguntar 😊",
        "Todo bien por aquí, ¿y tú?",
        "¡Excelente! ¿Cómo estás tú?"
    ],
    "¿qué puedes hacer?": [
        "Puedo responder a preguntas simples.",
        "Estoy aquí para conversar contigo.",
        "¡Pregúntame algo y te diré si lo entiendo!"
    ],
    "que puedes hacer": [
        "Puedo responder a preguntas simples.",
        "Estoy aquí para conversar contigo.",
        "¡Pregúntame algo y te diré si lo entiendo!"
    ],
    "adiós": [
        "¡Hasta luego! 😊",
        "¡Chao! Que tengas buen día.",
        "Adiós, fue un gusto hablar contigo."
    ],
    "adios": [
        "¡Hasta luego! 😊",
        "¡Chao! Que tengas buen día.",
        "Adiós, fue un gusto hablar contigo."
    ]
    
}

frases_conocidas = list(respuestas.keys())
preguntas_previas = set()
# Función para encontrar la mejor coincidencia

#Bucle de conversación
while True:
    user_input = input("Tú: ").lower().strip()# convertimos a minúsculas para facilitar la comparación

    if user_input == "salir":
        print(f"Chatbot: Conversación finalizada. ¡Nos vemos, {nombre}!")
        break

    # Buscamos la mejor coincidencia con fuzzy matching
    mejor_coincidencia, puntuacion, _ = process.extractOne(user_input, frases_conocidas)

    if puntuacion >= 80: #Puedes ajustar ese valor
        if mejor_coincidencia in preguntas_previas:
            respuesta = random.choice(respuestas[mejor_coincidencia])
            print("Chatbot: Ya me habías preguntado eso pero igual te respondo", respuesta)
        else:
            preguntas_previas.add(mejor_coincidencia)    
            respuesta = random.choice(respuestas[mejor_coincidencia])
            print("Chatbot:", respuesta)
    else:
        print("Chatbot: Lo siento, no entiendo esa pregunta.")
# Fin del código
