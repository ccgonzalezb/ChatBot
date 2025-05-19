#Librerias
import random

#Mensajes de bienvenida y despedida
print("Hola, soy un chatbot basado en reglas.")
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

#Bucle de conversación
while True:
    user_input = input("Tú: ").lower().strip()# convertimos a minúsculas para facilitar la comparación

    if user_input == "salir":
        print("Chatbot: Conversación finalizada.")
        break
    elif user_input in respuestas:
        respuesta = random.choice(respuestas[user_input])
        print("Chatbot:", respuesta)
    else:
        print("Chatbot: Lo siento, no entiendo esa pregunta.")
# Fin del código
