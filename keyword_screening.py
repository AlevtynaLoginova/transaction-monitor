# my keyword screening list - basically words that look sketchy in a memo
# TODO: probably need to expand this later, this is just a starter list
SUSPICIOUS_KEYWORDS = {
    "coin", "crypto", "bitcoin", "btc",
    "drugs", "pills", "weed", "cocaine",
    "gun", "firearm", "weapon",
}


def flag_suspicious_keywords(memo, keywords=SUSPICIOUS_KEYWORDS):
    # lowercase everything first, otherwise "COIN" won't match "coin"
    # learned this the hard way - string comparison is case sensitive by default
    memo_lower = memo.lower()

    # this is a list comprehension - basically a compressed for loop
    # "give me every word from my keyword list that shows up inside the memo"
    hits = [word for word in keywords if word in memo_lower]

    # if hits list has anything in it at all, python treats that as "truthy"
    # so this if just means "did we find at least one keyword?"
    if hits:
        # .join() glues list items together into one string, comma separated
        # so ['coin', 'bitcoin'] becomes "coin, bitcoin" - way more readable
        return f"FLAGGED: suspicious keyword(s) found: {', '.join(hits)}"

    return "OK"


def main():
    # just testing with one sample memo for now
    memo = "Payment for coin purchase, thanks!"
    result = flag_suspicious_keywords(memo)
    print(f"Memo: '{memo}' -> {result}")


if __name__ == "__main__":
    main()
