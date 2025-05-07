from mindmate_memory import ConversationMemory
from loss_events import mindmate_response

def main():
    memory = ConversationMemory()

    print("Mindmate: Hello! Let's chat. (Type 'exit' to quit)")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\nMindmate: Take care! See you soon! 👋")
            break
        
        # Get a context-aware response from Mindmate
        response = mindmate_response(user_input, memory)

        # Check if a follow-up is needed
        check_in = memory.should_check_in()
        if check_in:
            response = check_in
        
        # Store the interaction in memory
        memory.update_memory(user_input, response)
        memory.reset_check_in_flag()
        
        # Display response to user
        print(f"Mindmate: {response}")
    
    # Export conversation history when exiting
    memory.export_session()

if __name__ == "__main__":
    main()