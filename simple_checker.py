# 1. Variables — these hold the data for one transaction
amount = 15000
country = "Iran"

# 2. A list — the countries we consider high risk
high_risk_countries = ["Iran", "North Korea", "Syria", "Russia"]


# 3. A function — takes inputs, returns a decision
def check_transaction(amount, country):
    # 4. If/else — the actual decision logic
    if amount >= 10000 and country in high_risk_countries:
        return "SUSPICIOUS: large amount to a high-risk country"
    elif amount >= 10000:
        return "SUSPICIOUS: large amount"
    elif country in high_risk_countries:
        return "SUSPICIOUS: high-risk country"
    else:
        return "OK"


# 5. Print — show the result
result = check_transaction(amount, country)
print(f"Transaction of ${amount} to {country}: {result}")
