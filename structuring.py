def flag_near_threshold_pattern(amounts, threshold=10000, proximity=0.8, min_count=3):
    """Flag if multiple amounts sit suspiciously close to (but under) the threshold."""
    near_threshold = [a for a in amounts if proximity * threshold <= a < threshold]
    if len(near_threshold) >= min_count:
        return f"FLAGGED: {len(near_threshold)} transactions near reporting threshold"
    return "OK"


def flag_aggregate_over_threshold(amounts, threshold=10000):
    """Flag if the total of all amounts exceeds the threshold, even though no single one does."""
    total = sum(amounts)
    all_under = all(a < threshold for a in amounts)
    if all_under and total >= threshold:
        return f"FLAGGED: aggregate ${total} exceeds threshold despite no single large transaction"
    return "OK"


def evaluate_structuring(amounts):
    """Run all structuring-related rules and return a list of triggered flags."""
    flags = []

    pattern_flag = flag_near_threshold_pattern(amounts)
    if pattern_flag != "OK":
        flags.append(pattern_flag)

    aggregate_flag = flag_aggregate_over_threshold(amounts)
    if aggregate_flag != "OK":
        flags.append(aggregate_flag)

    return flags


def main():
    # Sample: someone breaking $28,000 into three chunks, each just under $10,000
    amounts = [9500, 9200, 9300]

    flags = evaluate_structuring(amounts)
    print(f"Structuring flags: {flags}")


if __name__ == "__main__":
    main()
