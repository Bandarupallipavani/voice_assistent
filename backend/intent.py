def detect_intent(text: str):
    text = text.lower()

    if "youtube" in text:
        return "OPEN_YOUTUBE"
    elif "google" in text:
        return "OPEN_GOOGLE"
    elif "search" in text:
        return "SEARCH"
    else:
        return "LLM"
