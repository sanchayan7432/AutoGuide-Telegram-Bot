def enforce_word_limit(answer, min_w, max_w):
    words = answer.split()

    if len(words) > max_w:
        words = words[:max_w]

    return " ".join(words)