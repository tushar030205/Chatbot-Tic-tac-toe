def chatbot_response(user_input):
    # Convert the user input to lowercase for easier matching
    user_input = user_input.lower()

    # Predefined responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here to help you!"
    elif "your name" in user_input:
        return "I'm ChatGPT, your virtual assistant."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "Sure! What do you need help with?"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Example interaction with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
