print("Hola, soy un chatbot basado en reglas.")
print("Escribe Salir para terminar la conversación.")

while True:
    user_input = input("Tú: ")
    user_input = user_input.lower()# convertimos a minúsculas para facilitar la comparación

    if user_input == "hola":
        print("Chatbot: ¡Hola! ¿Cómo estás?")
    elif user_input == "¿Cómo estás?" or user_input == "como estas":
        print("Chatbot: Estoy bien, gracias por preguntar.")
    elif user_input == "¿qué puedes hacer?" or user_input == "que puedes hacer":  
        print("Chatbot: Puedo responder preguntas simples, como esta.")
    elif user_input == "adiós" or user_input == "adios":
        print("Chatbot: ¡Hasta luego!")
        break
    elif user_input == "salir":
        print("Chatbot: Conversación finalizada.")
        break
    else:
        print("Chatbot: Lo siento, no entiendo esa pregunta.")
# Fin del código
