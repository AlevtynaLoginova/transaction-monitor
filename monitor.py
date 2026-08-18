import csv

from sanctions import flag_sanctioned_country, flag_high_risk_country

def main():
    transactions_by_account = {}

    with open("transactions.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            account = row["account_id"]
            amount = float(row["amount"])
            timestamp = float(row["timestamp"])
            country = row["country"]

            if account not in transactions_by_account:
                transactions_by_account[account] = []
            transactions_by_account[account].append(timestamp)

            flags = evaluate_transaction(amount, transactions_by_account[account])
            print(f"Account {account}, amount ${amount}: {flags}")


def flag_large_transaction(amount, threshold=10000):
    """Return a flag string if amount exceeds threshold, else 'OK'."""
    if amount >= threshold:
        return "FLAGGED: large transaction"
    return "OK"


def flag_velocity(timestamps, window_minutes=10, max_count=3):
    """Flag if more than max_count transactions occur within window_minutes of each other."""
    timestamps = sorted(timestamps)
    for i in range(len(timestamps)):
        count = 1
        for j in range(i + 1, len(timestamps)):
            if timestamps[j] - timestamps[i] <= window_minutes:
                count += 1
            else:
                break
        if count > max_count:
            return "FLAGGED: high velocity"
    return "OK"


def evaluate_transaction(amount, timestamps, country):  
    """Run all detection rules on a transaction and return a list of triggered flags."""
    flags = []

    amount_flag = flag_large_transaction(amount)
    if amount_flag != "OK":
        flags.append(amount_flag)

    velocity_flag = flag_velocity(timestamps)
    if velocity_flag != "OK":
        flags.append(velocity_flag)

    return flags


if __name__ == "__main__":
    main()
