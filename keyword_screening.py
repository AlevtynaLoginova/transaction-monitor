def flag_fuzzy_keywords(memo, keywords, threshold=0.8):
    """Check memo words against keyword list, scoring each as a fuzzy keyword hit."""
    memo_lower = memo.lower()
    memo_words = memo_lower.split()

    hits = []
    for keyword in keywords:
        for memo_word in memo_words:
            score = fuzzy_score(keyword, memo_word)
            if score >= threshold:
                hits.append((keyword, memo_word, round(score, 2)))

    if hits:
        # just calling these "keyword hits" now, score is baked into each one
        hit_strings = [f"{kw}~{mw} (score {score})" for kw, mw, score in hits]
        return f"KEYWORD HIT: {', '.join(hit_strings)}"
    return "OK"


def flag_all_typologies(memo, typologies=ALL_TYPOLOGIES, threshold=0.8):
    """Check memo against every typology category, return keyword hits grouped by type."""
    flags = []

    for typology_name, keywords in typologies.items():
        result = flag_fuzzy_keywords(memo, keywords, threshold)
        if result != "OK":
            flags.append(f"[{typology_name}] {result}")

    if flags:
        return flags
    return ["OK"]
