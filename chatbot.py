from flask import Flask, request, render_template
import wikipedia

app = Flask(__name__)

# FAQ Dictionary
faq_responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! Ask me anything.",
    "hey": "Hey! Nice to see you here.",
    "good morning": "Good morning! Have a productive day ",
    "good night": "Good night! Sweet dreams ",
    "how are you": "I'm just a bot, but I'm doing great! Thanks for asking.",
    "what is your name": "I'm a simple chatbot built with Flask.",
    "who created you": "I was created by developers who love Python and Flask!",
    "bye": "Goodbye! Have a nice day.",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "what can you do": "I can answer simple questions and fetch knowledge from Wikipedia!",
    "tell me a joke": "Why don’t programmers like nature? Too many bugs!",
    "where are you from": "I live inside your computer ",
    "what is flask": "Flask is a lightweight web framework for Python used to build web apps and APIs.",
    "what is ai": "AI stands for Artificial Intelligence — machines that can simulate human thinking.",
    "what is python": "Python is a powerful programming language, popular for AI, data science, and web development.",
    "what is machine learning": "Machine learning is teaching computers to learn patterns from data without explicit programming.",
    "what is deep learning": "Deep Learning is a subset of ML that uses neural networks to process complex data like images & speech.",
    "who is your favorite superhero": "I like Iron Man— he’s basically a mix of AI and tech genius.",
    "do you like pizza": "Of course!Especially with extra cheese!",
    "sing a song": " I can’t sing, but I can drop some beats: beep bop boop "
}

default_response = "I don’t know that. Let me check Wikipedia..."

chat_history = []

def get_wikipedia_answer(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.DisambiguationError as e:
        return f"Your question is too broad. Did you mean: {', '.join(e.options[:5])}?"
    except wikipedia.PageError:
        return "Sorry, I couldn't find anything on that topic."
    except:
        return "Oops! Something went wrong while fetching info."

@app.route("/", methods=["GET", "POST"])
def chatbot():
    global chat_history
    if request.method == "POST":
        user_input = request.form["message"].lower().strip()

        # Fuzzy matching for FAQ
        bot_response = None
        for key in faq_responses:
            if key in user_input:
                bot_response = faq_responses[key]
                break

        # Wikipedia fallback
        if not bot_response:
            bot_response = get_wikipedia_answer(user_input)

        # Save messages
        chat_history.append({"sender": "user", "text": request.form["message"]})
        chat_history.append({"sender": "bot", "text": bot_response})

    return render_template("index.html", chat_history=chat_history)

@app.route("/clear", methods=["POST"])
def clear_chat():
    global chat_history
    chat_history = []
    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
