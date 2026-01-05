def perform_action(intent: str, text: str):
    if intent == "OPEN_YOUTUBE":
        return {
            "response": "Opening YouTube",
            "url": "https://www.youtube.com"
        }

    elif intent == "OPEN_GOOGLE":
        return {
            "response": "Opening Google",
            "url": "https://www.google.com"
        }

    elif intent == "SEARCH":
        query = text.replace("search", "")
        return {
            "response": f"Searching for {query}",
            "url": f"https://www.google.com/search?q={query}"
        }

    else:
        return None
