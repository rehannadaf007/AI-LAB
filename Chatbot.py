import random
import re

class RuleBasedChatbot:
    def __init__(self):
        self.rules = {
            r'\b(hi|hello|hey|hola)\b': [
                "Hello! How can I help you today?",
                "Hey there! What's on your mind?",
                "Hi! Good to chat with you."
            ],
            r'\b(how are you|how\'s it going|how do you do)\b': [
                "I'm just a bundle of code, but I'm running smoothly! How are you?",
                "Doing great, thanks for asking! What can I do for you?"
            ],
            r'\b(what is your name|who are you|your name)\b': [
                "I am EchoBot, your friendly neighborhood rule-based assistant!",
                "You can call me EchoBot."
            ],
            r'\b(help|support|features)\b': [
                "I can answer basic greetings, tell you my name, or help you exit the chat.",
                "Right now, I'm configured for basic conversational rules. Ask me who I am!"
            ],
            r'\b(weather)\b': [
                "I don't have real-time internet access, but I hope it's sunny where you are!",
                "I'm stuck inside a computer terminal, so I can't quite tell!"
            ]
        }
        self.exit_commands = ["bye", "goodbye", "exit", "quit"]
        self.default_responses = [
            "I'm not quite sure I understand that. Could you rephrase it?",
            "Interesting... Can you tell me more about that?",
            "My rules don't cover that query yet, but I'm listening!"
        ]

    def match_intent(self, user_message):
        """Processes user input, searches for matching patterns, and returns a response."""
        user_message = user_message.lower().strip()
        if any(cmd in user_message for cmd in self.exit_commands):
            return "Goodbye! Have a wonderful day!"
        for pattern, responses in self.rules.items():
            if re.search(pattern, user_message):
                return random.choice(responses)
        return random.choice(self.default_responses)

    def start_chat(self):
        """Starts the interactive terminal chat loop."""
        print("="*50)
        print(" EchoBot: Hello! Type 'exit', 'quit', or 'bye' to leave.")
        print("="*50)
        
        while True:
            try:
                user_input = input("You: ")
                response = self.match_intent(user_input)
                print(f"EchoBot: {response}")
                if response == "Goodbye! Have a wonderful day!":
                    break
            except (KeyboardInterrupt, EOFError):
                print("\nEchoBot: Goodbye!")
                break
if __name__ == "__main__":
    bot = RuleBasedChatbot()
    bot.start_chat()