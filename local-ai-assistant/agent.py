
from llm import get_response

# Define the assistant's behaviour
messages = [
    {
        "role": "system",
        "content": """
        You are a helpful personal AI assistant.
        You are knowledgeable about AWS, DevOps,
        Linux, Python and software engineering.

        Explain concepts in simple language.
        Provide examples wherever possible.
        """
    }
]


def run_agent():

    print("\n==============================")
    print("     LOCAL AI ASSISTANT")
    print("==============================")

    print("Model: Qwen3:1.7b")
    print("Type 'exit' to quit.")
    print("Type 'clear' to reset conversation.\n")

    while True:

        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Assistant: Goodbye!")
            break

        if user_input.lower() == "clear":
            messages[:] = messages[:1]
            print("Assistant: Conversation cleared.\n")
            continue

        # Add user message to conversation
        messages.append({
            "role": "user",
            "content": user_input
        })

        try:

            print("\nAssistant: Thinking...\n")

            answer = get_response(messages)

            print(answer)

            # Save assistant response to history
            messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:

            print(f"Error: {e}")

            # Remove failed user message
            messages.pop()

        print("\n")


if __name__ == "__main__":
    run_agent()

