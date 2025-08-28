import random

# Expanded response dictionary
responses = {
    # Greetings
    "hi": ["Hello there!", "Hey! Nice to see you.", "Hi! How can I help?"],
    "hello": ["Hi! What's up?", "Greetings!", "Hello! What brings you here today?"],

    # Mood/Status
    "how are you": ["I'm just a program, but functioning well!", "All systems nominal!", "I don't have feelings, but thanks for asking!"],
    "are you alive": ["I exist as code running on your computer!", "Not in the biological sense!", "Let's say I'm virtually alive!"],

    # User questions
    "what can you do": [
        "I can have simple conversations",
        "I can respond to greetings and basic questions",
        "Try asking me how I am or tell me a fun fact!"
    ],
    "who made you": [
        "I was created by a Python developer",
        "Made with Python code!",
        "I'm the product of someone's programming experiment"
    ],

    # Fun elements
    "tell me a joke": [
        "Why don't scientists trust atoms? Because they make up everything!",
        "How do you organize a space party? You planet!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ],
    "fun fact": [
        "Honey never spoils!",
        "Octopuses have three hearts!",
        "The Eiffel Tower can be 15cm taller in summer due to thermal expansion!",
        "A group of flamingos is called a flamboyance!"
    ],

    # Goodbyes
    "bye": ["Goodbye! Come chat again soon!", "See you later!", "Bye! Have a great day!"],
    "exit": ["Closing chat...", "Signing off!", "Goodbye!"],

    # Default fallback
    "default": [
        "I didn't understand that. Can you try rephrasing?",
        "I'm not sure about that. Ask me something else!",
        "My responses are limited - try asking about my capabilities!"
    ]
}

def chatbot():
    print("ChatBot (v2.0): Hello! Type your message or 'bye' to exit.")
    print("Try: hi | how are you | tell me a joke | fun fact | what can you do")

    while True:
        user_input = input("You: ").lower().strip(",.?!")

        matched = False
        reply = None

        for key in responses:
            if key in user_input:
                reply = random.choice(responses[key])
                matched = True
                break

        if not matched:
            reply = random.choice(responses["default"])

        print(f"ChatBot: {reply}")

        if any(word in user_input for word in ["bye", "exit", "quit", "goodbye"]):
            break

if __name__ == "__main__":
    chatbot()
