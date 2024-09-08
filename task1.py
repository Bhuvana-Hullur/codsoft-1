rules = {
    "hello": "Hi! How can I assist you today?",
    "how are you": "I'm doing great, thanks for asking!",
    "what is your name": "I'm a simple chatbot, nice to meet you!",
    "can you help me":"offcourse,what can I help you",
    "what are chatbots used for":"chatbots are used in customer services,healthcare,education,and ecommerce to provide quick responses and automate tasks",
    "thankyou":"my pleaseure",
    "exit": "Goodbye! It was nice chatting with you."
}

def chatbot():
    print("Welcome to the chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("User: ").lower()
        
        
        if user_input in rules:
            print("Chatbot:", rules[user_input])
        elif user_input == "exit":
            print("Chatbot:", rules["exit"])
            break
        else:
            print("Chatbot: Sorry, I didn't understand that. Please try again!")

chatbot()
