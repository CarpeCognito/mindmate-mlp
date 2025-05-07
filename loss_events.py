import random

# Define keywords for event categories
LOSS_EVENT_KEYWORDS = {
    "pet_loss": {
        "loss": [
            "put down", "passed away", "lost", "died", "gone",
            "grieving", "old age", "euthanized"
        ],
        "context": [
            "cat", "dog", "pet", "rabbit", "hamster", "bird", "animal", "ferret"
        ]
    },
    "general_loss": {
        "loss": [
            "passed away", "died", "funeral", "grieving", "bereavement", "lost", "gone"
        ],
        "context": [
            "mom", "dad", "mother", "father", "friend", "sister",
            "brother", "partner", "husband", "wife"
        ]
    },
    # Easily extendable:
    # "breakup": {...},
    # "job_loss": {...},
}

# Responses mapped to event type
LOSS_RESPONSES = {
    "pet_loss": [
        "I'm so sorry about your pet. Losing a companion like that is incredibly hard. Would you like to talk about her?",
        "Losing a pet is like losing a family member. I’m here for you—want to share more about your cat?",
        "That’s heartbreaking. If you feel like talking or remembering some good times, I’m here to listen."
    ],
    "general_loss": [
        "I'm so sorry for your loss. If you want to talk or just need someone to listen, I'm here.",
        "Losing someone is never easy. Take your time—I'm here if you need to talk.",
        "That sounds really tough. If you want to share more or just need support, I'm here for you."
    ]
}

def detect_loss_event(text):
    """
    Detects if user input mentions a loss-related event.
    Returns the loss category if detected, otherwise None.
    """
    text_lower = text.lower()
    for category, keywords in LOSS_EVENT_KEYWORDS.items():
        if any(loss_kw in text_lower for loss_kw in keywords["loss"]) and \
           any(ctx_kw in text_lower for ctx_kw in keywords["context"]):
            return category
    return None

def mindmate_response(user_input, session_state, detect_sentiment):
    """
    Generates a context-aware response based on user input.
    Prioritizes grief-related events, then general mood sentiment.
    """
    mood, intensity = detect_sentiment(user_input)
    loss_event = detect_loss_event(user_input)

    if loss_event in LOSS_RESPONSES:
        return random.choice(LOSS_RESPONSES[loss_event])
    elif mood == "grief":
        return "I'm here to listen if things feel heavy. How can I help?"
    elif mood == "positive":
        return "That's wonderful! What's been making you feel this way?"
    else:
        return "I'm here for whatever you need—feel free to share."