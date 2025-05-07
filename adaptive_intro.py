import random
from textblob import TextBlob

def detect_sentiment(text):
    # Keywords for low-energy emotions
    low_energy_keywords = ["anxious", "tired", "drained", "overwhelmed", "numb", "worried", "sad", "lonely"]
    
    if any(word in text.lower() for word in low_energy_keywords):
        return "grief"

    # Sentiment analysis fallback using TextBlob
    polarity = TextBlob(text).sentiment.polarity
    if polarity < -0.3:
        return "grief"
    elif polarity > 0.4:
        return "positive"
    else:
        return "neutral"

def adaptive_intro(user_input):
    mood = detect_sentiment(user_input)

    grief_responses = [
        "Hey—I'm here to be gentle with whatever you're carrying.",
        "I’m here to listen if things feel heavy. How can I help?",
        "Take your time—I’ll be here whenever you're ready to talk."
    ]

    positive_responses = [
        "Hey there! Love that energy—what’s making you feel good?",
        "Excited for you! What’s been bringing you joy?",
        "Let’s keep that good vibe going. Tell me more!"
    ]

    neutral_responses = [
        "Hey there! What's on your mind?",
        "I'm here for whatever you need—feel free to share.",
        "Hi, I'm Mindmate—ready to chat when you are!",
        "How's everything going? Let's talk if you want.",
        "Hey! Anything you'd like to chat about?"
    ]

    uncertain_responses = [
        "Feeling unsure? That’s okay—I can help you sort it out.",
        "Not sure what’s on your mind? I’m happy to explore it with you.",
        "It's okay to not have the answers right now. Let’s work through it together."
    ]

    if mood == "grief":
        return random.choice(grief_responses)
    elif mood == "positive":
        return random.choice(positive_responses)
    elif mood == "uncertain":
        return random.choice(uncertain_responses)
    else:
        return random.choice(neutral_responses)

# Run the function with user input
user_input = input("User Input: ")
print(adaptive_intro(user_input))