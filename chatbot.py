"""
DECODELABS AI CHATBOT
Project 1: Rule-Based Artificial Intelligence
"""

import time
import sys
import random
from datetime import datetime
import string
import os

# ============================================================================
# CONFIGURATION
# ============================================================================

class Config:
    """System configuration and constants"""
    TYPING_SPEED = 0.03
    BOT_NAME = "DecodeLabs AI"
    VERSION = "1.0"
    COMPANY = "DecodeLabs"
    LOG_FILE = "chat_session.log"
    
    COLORS = {
        "reset": "\033[0m",
        "bold": "\033[1m",
        "dim": "\033[2m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
    }
    
    if os.name == 'nt':
        os.system('color')


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def colorize(text, color_name):
    """Add color to text for terminal output"""
    color_code = Config.COLORS.get(color_name, Config.COLORS["reset"])
    return f"{color_code}{text}{Config.COLORS['reset']}"


def typewriter_effect(text, color="green"):
    """Print text with typing animation"""
    colored_text = colorize(text, color)
    for char in colored_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(Config.TYPING_SPEED)
    print()


def sanitize_input(raw_input):
    """Clean and normalize user input"""
    if not raw_input or raw_input.strip() == "":
        return ""
    cleaned = raw_input.strip().lower()
    cleaned = cleaned.translate(str.maketrans('', '', string.punctuation))
    cleaned = ' '.join(cleaned.split())
    return cleaned


def log_conversation(user_input, bot_response):
    """Save conversation to log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(Config.LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] USER: {user_input}\n")
            f.write(f"[{timestamp}] BOT: {bot_response}\n")
            f.write("-" * 80 + "\n")
    except:
        pass


def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


# ============================================================================
# HELP AND INFO FUNCTIONS
# ============================================================================

def get_help_menu():
    """Generate help menu"""
    return """
+-----------------------------------------------------------------------------+
|                            COMMAND REFERENCE                                |
+-----------------------------------------------------------------------------+
|                                                                             |
|  GREETINGS                                                                  |
|     - hello, hi, hey, good morning, good evening                           |
|                                                                             |
|  EXIT                                                                       |
|     - exit, quit, end, bye, goodbye, terminate, stop, close                |
|                                                                             |
|  ABOUT ME                                                                   |
|     - who are you, what are you, your name, who made you, who built you     |
|                                                                             |
|  AI CONCEPTS                                                                |
|     - what is ai, what is machine learning                                  |
|     - what is deep learning, what is nlp                                    |
|     - rule based system, generative ai                                      |
|     - white box, deterministic vs probabilistic, guardrails                 |
|                                                                             |
|  COMPANY                                                                     |
|     - what is decodelabs, about decodelabs, what is project 1               |
|                                                                             |
|  UTILITIES                                                                  |
|     - help, commands, menu, what can you do, features                       |
|     - history, status, clear                                                |
|     - tell me a joke, more jokes, motivate me, thank you, ping              |
|                                                                             |
+-----------------------------------------------------------------------------+
"""


def get_status():
    """Show system status"""
    return f"""
+-----------------------------------------------------------------------------+
|                              SYSTEM STATUS                                  |
+-----------------------------------------------------------------------------+
|  - Name: {Config.BOT_NAME}                                                  
|  - Creator: {Config.COMPANY}                                                
|  - Status: Online                                                           
+-----------------------------------------------------------------------------+
"""


def get_capabilities():
    """Show system capabilities"""
    return f"""
+-----------------------------------------------------------------------------+
|                            WHAT I CAN DO                                    |
+-----------------------------------------------------------------------------+
|                                                                             |
|  • Answer questions about AI and machine learning                          |
|  • Tell you about DecodeLabs and Project 1                                 |
|  • Share jokes and motivation                                               |
|  • Remember our conversation history                                        |
|  • Save our chat to a log file                                              |
|                                                                             |
|  Just type 'help' anytime to see all commands!                             |
|                                                                             |
+-----------------------------------------------------------------------------+
"""


# ============================================================================
# KNOWLEDGE BASE (RESPONSES DICTIONARY)
# ============================================================================

RESPONSES = {
    # GREETINGS
    "hello": "Hey there! How can I help you today?",
    "hi": "Hi! Welcome to DecodeLabs. What would you like to know?",
    "hey": "Hey! Ready to learn about AI?",
    "good morning": "Good morning! Hope you're having a great day.",
    "good evening": "Good evening! Ready to do some coding?",
    
    # FAREWELLS
    "bye": "Take care! Come back anytime.",
    "goodbye": "Goodbye! Feel free to return if you have more questions.",
    
    # PERSONAL
    "who are you": f"I'm {Config.BOT_NAME}, a simple chatbot I built as my first project at DecodeLabs.",
    "what are you": f"I'm a rule-based chatbot. That means I respond to specific commands you type.",
    "your name": f"My name is {Config.BOT_NAME}. Nice to meet you!",
    "who made you": f"I was created by a student at {Config.COMPANY} as part of their AI training.",
    "who built you": f"The students and instructors at {Config.COMPANY} built me.",
    "ping": "Pong! I'm here and ready to chat.",
    "how are you": "I'm functioning perfectly! Ready to help you learn about AI.",
    
    # AI CONCEPTS
    "what is ai": "AI stands for Artificial Intelligence. It's about making computers smart enough to do things that normally need human intelligence, like understanding language or recognizing images.",
    "what is machine learning": "Machine Learning is a way for computers to learn from data instead of being told exactly what to do. For example, showing a computer many photos of cats so it learns to recognize cats on its own.",
    "what is deep learning": "Deep Learning is a more advanced type of machine learning that uses brain-like networks to figure out complex patterns. It's what powers things like voice assistants and self-driving cars.",
    "what is nlp": "NLP stands for Natural Language Processing. It helps computers understand, interpret, and respond to human language. I use basic NLP to understand your commands.",
    "what is a rule based system": "A rule-based system is exactly what I am! I have a set of predefined rules (or commands) that I follow. If you say something I know, I respond. If not, I let you know I don't understand.",
    "what is generative ai": "Generative AI is the technology that can create new things like text, images, or music. ChatGPT is a famous example. It learns patterns from lots of data and then creates something new based on what it learned.",
    "what is a white box": "A white box system is transparent - you can see exactly how it works. Rule-based systems like me are white boxes! You can trace exactly why I give certain responses because I follow clear rules.",
    "deterministic vs probabilistic": "Deterministic = same answer every time (me!). Probabilistic = answers may vary (like ChatGPT). Both have their uses.",
    "guardrails": "AI guardrails act as deterministic filters for probabilistic outputs, ensuring compliance and safety.",
    "what are guardrails": "Guardrails are safety rules that prevent AI from giving harmful or incorrect responses.",
    "what is the ipo model": "IPO stands for Input → Process → Output. It's the fundamental framework for any AI system.",
    
    # COMPANY
    "what is decodelabs": f"{Config.COMPANY} is an AI training center in Lucknow, India where students learn AI by building real projects.",
    "about decodelabs": f"{Config.COMPANY} focuses on hands-on learning. Students don't just study theory - they actually build working AI systems.",
    "what is project 1": "Project 1 is building a rule-based chatbot like me! It teaches the basics of how AI systems make decisions.",
    
    # UTILITIES
    "help": get_help_menu(),
    "commands": get_help_menu(),
    "menu": get_help_menu(),
    "what can you do": get_capabilities(),
    "features": get_capabilities(),
    "status": get_status(),
    
    # EXIT COMMANDS (as responses)
    "end": "Goodbye! Keep learning and building AI systems! 👋",
    "terminate": "Terminating chat. Stay curious and keep coding! 🤖",
    "stop": "Stopping the conversation. Come back anytime!",
    "close": "Closing chat session. Take care and keep learning!",
    
    # JOKES AND FUN
    "tell me a joke": "Why did the programmer quit his job? Because he didn't get arrays of appreciation!",
    "tell me joke": "What do you call a computer that sings? A Dell!",
    "more jokes": "Why do Python programmers prefer dark mode? Because light attracts bugs!\n\nHere's another: What do you call a fake noodle? An impasta!",
    "motivate me": "You've got this! Every expert was once a beginner. Just keep going, one step at a time.",
    "motivation": "The secret to success is to start before you're ready. You're already doing great by building real projects!",
    "thank you": "You're very welcome! Happy to help.",
    "thanks": "Anytime! That's what I'm here for.",
}

# Exit commands list
EXIT_COMMANDS = ["exit", "quit", "end", "bye", "goodbye", "terminate", "stop", "close"]


# ============================================================================
# CONVERSATION MANAGER
# ============================================================================

class ConversationManager:
    def __init__(self, max_history=10):
        self.history = []
        self.max_history = max_history
        self.session_start = datetime.now()
        self.message_count = 0
    
    def add_exchange(self, user_msg, bot_msg):
        self.history.append({
            "user": user_msg,
            "bot": bot_msg,
            "timestamp": datetime.now()
        })
        self.message_count += 1
        if len(self.history) > self.max_history:
            self.history.pop(0)
    
    def get_session_duration(self):
        return datetime.now() - self.session_start
    
    def display_history(self):
        if not self.history:
            return colorize("\nNo conversation yet. Say something first!", "dim")
        
        output = "\n" + colorize("=" * 50, "cyan") + "\n"
        output += colorize("RECENT CONVERSATION\n", "bold")
        output += colorize("=" * 50, "cyan") + "\n\n"
        
        for exchange in self.history[-5:]:
            time_str = exchange["timestamp"].strftime("%H:%M:%S")
            output += colorize(f"[{time_str}] ", "dim")
            output += colorize("You", "yellow") + f": {exchange['user']}\n"
            output += colorize("      ", "dim")
            output += colorize("Me", "green") + f": {exchange['bot'][:60]}"
            if len(exchange['bot']) > 60:
                output += "..."
            output += "\n\n"
        
        return output


# ============================================================================
# CHATBOT ENGINE
# ============================================================================

class RuleBasedChatbot:
    def __init__(self):
        self.conversation = ConversationManager()
        self.is_running = True
    
    def generate_response(self, user_input):
        """Generate response based on input"""
        if user_input == "history":
            return self.conversation.display_history()
        
        if user_input == "clear":
            return "CLEAR_SCREEN"
        
        if user_input in RESPONSES:
            return RESPONSES[user_input]
        else:
            fallbacks = [
                f"Hmm, I don't know what '{user_input}' means. Try typing 'help' to see what I can do.",
                "Sorry, I don't understand that command. Type 'help' to see all my commands.",
                "I'm still learning! I don't recognize that. Try 'help' for things you can ask me.",
                "Not sure about that one. Type 'help' and I'll show you what I know."
            ]
            return random.choice(fallbacks)
    
    def display_welcome(self):
        """Show welcome screen"""
        clear_screen()
        print()
        print(colorize("=" * 50, "cyan"))
        print(colorize(f"  {Config.COMPANY} - AI Chatbot", "bold"))
        print(colorize("=" * 50, "cyan"))
        print()
        typewriter_effect(f"Hi! I'm {Config.BOT_NAME}.", "green")
        print()
        typewriter_effect("I can answer questions about AI, tell you about DecodeLabs, share some jokes, or just chat.")
        typewriter_effect(f"Type {colorize('help', 'yellow')} to see what I can do, or {colorize('exit', 'red')} to quit.")
        print()
        print(colorize("-" * 50, "dim"))
        print()
    
    def display_exit(self):
        """Show exit screen with stats"""
        duration = self.conversation.get_session_duration()
        minutes = duration.seconds // 60
        seconds = duration.seconds % 60
        print()
        print(colorize("=" * 50, "cyan"))
        print(colorize("  Thanks for chatting!", "bold"))
        if self.conversation.message_count > 0:
            print(colorize(f"  We had {self.conversation.message_count} messages in {minutes}m {seconds}s", "dim"))
        print(colorize("  Come back anytime!", "green"))
        print(colorize("=" * 50, "cyan"))
        print()
    
    def run(self):
        """Main loop"""
        self.display_welcome()
        
        while self.is_running:
            try:
                # Get input
                user_input = input(colorize("You: ", "yellow"))
                clean_input = sanitize_input(user_input)
                
                # Check exit
                if clean_input in EXIT_COMMANDS:
                    typewriter_effect("Goodbye! Take care.", "green")
                    self.is_running = False
                    break
                
                # Handle empty
                if not clean_input:
                    typewriter_effect("Go ahead, ask me something! Type 'help' if you're not sure what to ask.", "dim")
                    print()
                    continue
                
                # Get response
                response = self.generate_response(clean_input)
                
                # Handle clear screen
                if response == "CLEAR_SCREEN":
                    clear_screen()
                    self.display_welcome()
                    continue
                
                # Log and store
                log_conversation(user_input, response)
                self.conversation.add_exchange(user_input, response)
                
                # Display response
                print(colorize("Me: ", "green"), end="")
                typewriter_effect(response, "white")
                print()
                
            except KeyboardInterrupt:
                print("\n")
                typewriter_effect("Okay, stopping here. Take care!", "yellow")
                self.is_running = False
                break
            except Exception as e:
                print(colorize(f"Oops, something went wrong: {e}", "red"))
                print()
        
        self.display_exit()


# ============================================================================
# RUN
# ============================================================================

if __name__ == "__main__":
    chatbot = RuleBasedChatbot()
    chatbot.run()
