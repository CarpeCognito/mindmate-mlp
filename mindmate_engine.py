import re
import random
from collections import Counter

def detect_sentiment(text):
    """
    Detects sentiment in user input, prioritizing grief and strong emotions.
    Uses regex word boundaries for accuracy in phrase matching.
    """
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)

    grief_phrases = ["lost a friend", "passed away", "death", "mourning", "grief", "bereaved", "heartbroken", "devastated"]
    negative_words = ["stuck", "tired", "exhausted", "frustrated", "down", "angry", "rage", "furious", "broken", "hurt", "overwhelmed"]
    positive_words = ["energized", "excited", "happy", "motivated", "great"]

    for phrase in grief_phrases:
        pattern = r'\b' + re.escape(phrase) + r'\b'
        if re.search(pattern, text):
            return "grief"

    if any(word in words for word in negative_words):
        return "negative"

    if any(word in words for word in positive_words):
        return "positive"

    return "neutral"

def detect_repeated_keywords(user_input, session_state):
    """
    Tracks emotional progression rather than just repetition.
    Recognizes if grief transitions into anger and ensures meaningful response shifts.
    """
    if "history" not in session_state or not session_state["history"]:
        return False

    history = session_state["history"]
    previous_sentiment = detect_sentiment(history[-1]) if history else None
    current_sentiment = detect_sentiment(user_input)

    if previous_sentiment == "grief" and current_sentiment == "negative":
        return "grief_to_anger"

    return False

def mindmate_generate_response(user_input, session_state):
    """
    Generates emotionally intelligent responses while maintaining fluid conversation progression.
    Evolves responses to ensure engagement rather than repeating static phrases.
    """
    sentiment = detect_sentiment(user_input)
    repeated_theme = detect_repeated_keywords(user_input, session_state)

    response_pool = {
        "grief": [
            "That’s a heavy loss—I’m really sorry you're going through this.",
            "Losing someone close is incredibly hard—what’s sitting with you most?",
            "Grief comes in waves—there’s no right way to feel. Just take your time.",
            "That pain is real, and it matters. I'm here to sit with you in it.",
            "I know this is still hard. Have things shifted for you since then?",
            "My heart goes out to you. Rage is a natural part of grief—how are you experiencing it?",
            "That's a devastating loss. It's understandable to feel this deeply. I’m here if you need to share."
        ],
        "grief_to_anger": [
            "I notice your grief shifting into anger—that's a normal part of loss. Want to explore what's fueling that?",
            "Anger can be tied to loss. Would it help to talk through what’s been sitting with you?",
            "Grief can shift into frustration over time—what’s been weighing on you the most?"
        ],
        "negative": [
            "It’s okay to feel this—what’s been fueling your frustration?",
            "Anger and exhaustion build up—want to unpack what’s behind it?",
            "That sounds really tough—sometimes just acknowledging it helps.",
            "I'm sorry to hear that. What’s been difficult?",
            "That sounds tough. Want to talk through it?",
            "It’s okay to not be okay. I'm here to listen."
        ],
        "positive": [
            "Love that energy! What’s fueling this momentum?",
            "You're on fire today—what’s been pushing you forward?",
            "That excitement is contagious—where’s it coming from?",
            "That’s great to hear! What’s been making you feel good?",
            "Wonderful! Tell me more about what’s positive right now.",
            "Excellent! Let’s hold onto that feeling."
        ],
        "neutral": [
            "Life isn’t always clear-cut. Let’s sit with whatever’s showing up.",
            "You’re feeling something in between—and that’s okay. Let’s explore it.",
            "Not everything fits neatly into a box—how does it feel to sit with this?"
        ]
    }

    # Handle grief and emotional transitions
    if sentiment == "grief":
        if session_state.get("grief_persistent", False):
            return "Grief doesn’t just disappear. It evolves. What’s been different in how you’ve been processing it?"
        else:
            session_state["grief_persistent"] = True
            return random.choice(response_pool["grief"])

    if repeated_theme == "grief_to_anger":
        return random.choice(response_pool["grief_to_anger"])

    if sentiment == "negative":
        return random.choice(response_pool["negative"])

    # Avoid repeating the same response consecutively
    response = random.choice(response_pool.get(sentiment, response_pool["neutral"]))
    while response == session_state.get("last_response", ""):
        response = random.choice(response_pool.get(sentiment, response_pool["neutral"]))
    
    session_state["last_response"] = response
    return response

if __name__ == "__main__":
    session_state = {"history": []}

    while True:
        user_input = input("User Input: ").strip()
        if not user_input:
            print("I’m here whenever you’re ready—take your time.")
            continue

        session_state["history"].append(user_input)
        response = mindmate_generate_response(user_input, session_state)
        print(f"Mindmate Response: {response}")