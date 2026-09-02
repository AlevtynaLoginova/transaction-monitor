# keyword screening for suspicious transaction memos
# uses fuzzy matching (via difflib) so misspellings/obfuscation still get caught,
# not just exact spelling matches

from difflib import SequenceMatcher

# keyword lists, grouped by typology
# each typology = a different kind of illicit activity we're watching for

DRUG_KEYWORDS = {
    "drugs", "cocaine", "heroin", "meth", "fentanyl", "weed",
    "marijuana", "pills", "narcotics", "opioid",
}

HUMAN_TRAFFICKING_KEYWORDS = {
    "escort", "massage", "modeling", "visa sponsor", "labor camp",
    "domestic worker", "recruitment fee", "passport hold", "debt bondage",
}

# smuggling is NOT the same as trafficking - smuggling is about movement/transport,
# trafficking is about exploitation once someone's there. keeping separate on purpose
HUMAN_SMUGGLING_KEYWORDS = {
    "border crossing", "transport fee", "guide fee", "safe house",
    "coyote", "crossing fee",
}

WEAPONS_KEYWORDS = {
    "gun", "firearm", "weapon", "ammunition", "rifle", "explosive",
}

CRYPTO_EVASION_KEYWORDS = {
    "coin", "crypto", "bitcoin", "btc", "wallet transfer", "p2p exchange",
}

TERRORISM_FINANCING_KEYWORDS = {
    # real lists here use actual designated org name fragments -
    # these are generic placeholder terms just for practice
    "charity fund", "relief fund", "brotherhood", "foundation transfer",
}

SHELL_COMPANY_KEYWORDS = {
    "consulting fee", "holdings transfer", "trading account",
    "advisory services", "general services",
}

WILDLIFE_CRIME_KEYWORDS = {
    "ivory", "exotic animal", "rhino horn", "timber export", "endangered species",
}

GAMBLING_KEYWORDS = {
    "casino", "bet", "wager", "sportsbook", "poker deposit",
}

# one combined lookup so we can screen a memo against every typology at once
ALL_TYPOLOGIES = {
    "drugs": DRUG_KEYWORDS,
    "human_trafficking": HUMAN_TRAFFICKING_KEYWORDS,
    "human_smuggling": HUMAN_SMUGGLING_KEYWORDS,
    "weapons": WEAPONS_KEYWORDS,
    "crypto_evasion": CRYPTO_EVASION_KEYWORDS,
    "terrorism_financing": TERRORISM_FINANCING_KEYWORDS,
    "shell_company": SHELL_COMPANY_KEYWORDS,
    "wildlife_crime": WILDLIFE_CRIME_KEYWORDS,
    "gambling": GAMBLING_KEYWORDS,
}


def keyword_similarity(keyword, memo_word):
    # SequenceMatcher compares two strings, gives similarity ratio 0.0 to 1.0
    # 1.0 = identical, 0.0 = completely different
    return SequenceMatcher(None, keyword, memo_word).ratio()


def screen_memo_for_keywords(memo, keywords, threshold=0.8):
    """Screen a memo for keyword hits, allowing near-matches via similarity score."""
    memo_lower = memo.lower()
    memo_words = memo_lower.split()

    # known limitation: multi-word keywords (like "border crossing") won't match
    # well here since we're comparing single memo_words - fix later with phrase matching

    hits = []
    for keyword in keywords:
        for memo_word in memo_words:
            score = keyword_similarity(keyword, memo_word)
            if score >= threshold:
                hits.append((keyword, memo_word, round(score, 2)))

    if hits:
        hit_strings = [f"{kw}~{mw} (score {score})" for kw, mw, score in hits]
        return f"KEYWORD HIT: {', '.join(hit_strings)}"
    return "OK"


def screen_memo_all_typologies(memo, typologies=ALL_TYPOLOGIES, threshold=0.8):
    """Screen a memo against every typology's keyword list, tagging hits by type."""
    flags = []

    for typology_name, keywords in typologies.items():
        result = screen_memo_for_keywords(memo, keywords, threshold)
        if result != "OK":
            flags.append(f"[{typology_name}] {result}")

    if flags:
        return flags
    return ["OK"]


def main():
    test_memos = [
        "payment for raccoin purchase",
        "sending btc for services",
        "escort service fee payment",
        "modeling agency recruitment",
        "firearm purchase deposit",
        "casino deposit for weekend",
        "consulting fee invoice",
        "regular lunch payment",  # clean, should stay OK
    ]

    for memo in test_memos:
        results = screen_memo_all_typologies(memo)
        print(f"Memo: '{memo}'")
        for r in results:
            print(f"  -> {r}")
        print()


if __name__ == "__main__":
    main()
