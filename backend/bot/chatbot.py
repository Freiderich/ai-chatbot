def get_bot_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! I'm your pixel-AI assistant!"
    if "help" in message:
        return "Sure! What do you need help with?"
    if "bye" in message:
        return "Goodbye! See you later!"

    return "Hmm... I don't know that yet. But I'm learning!"
