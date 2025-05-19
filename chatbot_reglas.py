#Mensajes de bienvenida y despedida
print("Hola, soy un chatbot basado en reglas.")
print("Escribe Salir para terminar la conversación.")

#Diccionario con reglas
respuestas = {
    "hola":"¡Hola! ¿Cómo estás?",
    "¿cómo estás?":"Estoy bien, gracias por preguntar.",
    "como estas":"Estoy bien, gracias por preguntar.",
    "¿qué puedes hacer?":"Puedo responder preguntas simples, como esta.",
    "que puedes hacer":"Puedo responder preguntas simples, como esta.",
    "adiós":"¡Hasta luego!",
    "adios":"¡Hasta luego!",
}
#Bucle de conversación
while True:
    user_input = input("Tú: ")
    user_input = user_input.lower().strip()# convertimos a minúsculas para facilitar la comparación

    if user_input == "salir":
        print("Chatbot: Conversación finalizada.")
        break
    elif user_input in respuestas:
        print("Chatbot:", respuestas[user_input])
    else:
        print("Chatbot: Lo siento, no entiendo esa pregunta.")
# Fin del código
