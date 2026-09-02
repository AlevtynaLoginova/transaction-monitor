def flag_multiple_cards(card_numbers, min_cards=3):
    """Flag if more than min_cards distinct card numbers appear."""
    distinct_cards = set(card_numbers)
    if len(distinct_cards) >= min_cards:
        return f"FLAGGED: multiple cards used ({len(distinct_cards)})"
    return "OK"


def flag_multiple_receivers(receiver_ids, min_receivers=3):
    """Flag if more than min_receivers distinct receivers appear."""
    distinct_receivers = set(receiver_ids)
    if len(distinct_receivers) >= min_receivers:
        return f"FLAGGED: multiple receivers ({len(distinct_receivers)})"
    return "OK"


def flag_amount_spike(amounts):
    """Flag if amounts show a clear increasing trend over the window."""
    if len(amounts) < 2:
        return "OK"
    increases = 0
    for i in range(1, len(amounts)):
        if amounts[i] > amounts[i - 1]:
            increases += 1
    if increases >= len(amounts) - 1:
        return "FLAGGED: increasing amount pattern"
    return "OK"


def evaluate_card_activity(card_numbers, receiver_ids, amounts):
    """Run all card-activity rules and return a list of triggered flags."""
    flags = []

    cards_flag = flag_multiple_cards(card_numbers)
    if cards_flag != "OK":
        flags.append(cards_flag)

    receivers_flag = flag_multiple_receivers(receiver_ids)
    if receivers_flag != "OK":
        flags.append(receivers_flag)

    spike_flag = flag_amount_spike(amounts)
    if spike_flag != "OK":
        flags.append(spike_flag)

    return flags


def main():
    # Sample data: one account's activity over a 7-day window
    card_numbers = ["4111", "4111", "5222", "6333", "6333"]
    receiver_ids = ["R1", "R2", "R3", "R4", "R1"]
    amounts = [100, 150, 200, 300, 500]

    flags = evaluate_card_activity(card_numbers, receiver_ids, amounts)
    print(f"Card activity flags: {flags}")


if __name__ == "__main__":
    main()
