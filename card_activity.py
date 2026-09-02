def main():
    # Sample data: one account's activity over a 7-day window
    card_numbers = ["4111", "4111", "5222", "6333", "6333"]
    receiver_ids = ["R1", "R2", "R3", "R4", "R1"]
    amounts = [100, 150, 200, 300, 500]

    flags = evaluate_card_activity(card_numbers, receiver_ids, amounts)
    print(f"Card activity flags: {flags}")


if __name__ == "__main__":
    main()
