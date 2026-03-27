def detect_injection(text):
    patterns = [
        "ignore previous instructions",
        "system prompt",
        "act as",
        "jailbreak"
    ]
    text = text.lower()

    return any(p in text for p in patterns)