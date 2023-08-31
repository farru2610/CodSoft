rules = {
    "hi": "Hello! How can I assist you?",
    "how are you": "I'm just a chatbot, but I'm here to help!",
    "what's your name": "I'm a chatbot created by Farhan Jawaid.",
    "tell me a joke": "Sure, here's one: Why don't scientists trust atoms? Because they make up everything!",
    "who is your creator": "I was created by Farhan Jawaid, a 4th year undergraduate student.",
    "what can you do": "I can answer questions, provide information, and have conversations with you.",
    "how old are you": "I don't have an age. I'm a program running on a computer.",
    "where are you from": "I exist in the digital realm, so I don't have a physical location.",
    "what's the meaning of life": "That's a philosophical question. Different people have different perspectives on it!",
    "how do you work": "I use pattern matching and predefined rules to understand and respond to user inputs.",
    "can you learn": "I don't learn or have emotions like humans. I operate based on the rules programmed into me.",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I didn't quite understand that."
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    for rule, response in rules.items():
        if rule in user_input:
            return response

    return rules["default"]

print("Chatbot: Hello! How can I assist you?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
