import json
import random

class ConversationMemory:
    def __init__(self):
        self.recent_events = []

    def add_event(self, event, topic):
        """Stores recent events for context tracking."""
        self.recent_events.append({'event': event, 'topic': topic})
        self.recent_events = self.recent_events[-3:]

    def get_active_thread(self):
        """Returns the most relevant topic (last mentioned)."""
        return sorted(self.recent_events, key=lambda x: x.get('last_mentioned', 0), reverse=True)[0] if self.recent_events else None

    def decay_context(self):
        """Removes outdated topics if unrelated conversations continue."""
        if len(self.recent_events) > 3:
            self.recent_events.pop(0)

TOPIC_SYNONYMS = {
    "cat": ["meow", "purring", "kitten"],
    "dog": ["bark", "puppy", "fetch"],
    "cousin": ["family", "relative", "visit"]
}

def is_followup_about_topic(user_input, topic):
    """Checks if user input relates to a stored topic using keyword matching."""
    synonyms = TOPIC_SYNONYMS.get(topic, []) + [topic]
    return any(word in user_input.lower() for word in synonyms)

def mindmate_response(user_input, memory):
    """Generates responses based on stored memory threads and detected topics."""
    active_thread = memory.get_active_thread()
    
    if active_thread and is_followup_about_topic(user_input, active_thread['topic']):
        return f"It’s understandable to miss your {active_thread['topic']}. Want to share a memory?"
    
    return random.choice(["I'm here for whatever you need.", "That’s really tough. How are you feeling now?"])

def export_session_log(memory, filename="mindmate_session.json"):
    """Saves recent events as a JSON file for analysis."""
    with open(filename, "w") as f:
        json.dump(memory.recent_events, f, indent=4)

if __name__ == "__main__":
    memory = ConversationMemory()
    export_session_log(memory)