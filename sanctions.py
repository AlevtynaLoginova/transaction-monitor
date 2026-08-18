SANCTIONED_COUNTRIES = {
    "Iran",
    "North Korea",
    "Syria",
    "Cuba",
    "Russia",
    "Crimea",
    "Donetsk",
    "Luhansk",
}

HIGH_RISK_COUNTRIES = {
    "Afghanistan": 8,
    "Myanmar": 8,
    "Venezuela": 7,
    "Yemen": 7,
    "Nigeria": 6,
    "Pakistan": 6,
    "UAE": 5,
}


def flag_sanctioned_country(country, sanctioned_list=SANCTIONED_COUNTRIES):
    """Return a flag string if country is on the sanctions list, else 'OK'."""
    if country in sanctioned_list:
        return "FLAGGED: sanctioned country"
    return "OK"


def flag_high_risk_country(country, risk_scores=HIGH_RISK_COUNTRIES, threshold=5):
    """Return a flag string if country's risk score meets/exceeds threshold, else 'OK'."""
    score = risk_scores.get(country, 0)
    if score >= threshold:
        return f"FLAGGED: high-risk country (score {score})"
    return "OK"
