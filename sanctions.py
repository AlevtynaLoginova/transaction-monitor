HIGH_RISK_COUNTRIES = {
    "Iran",
    "North Korea",
    "Syria",
    "Cuba",
    "Russia",
}


def flag_sanctioned_country(country, high_risk_list=HIGH_RISK_COUNTRIES):
    """Return a flag string if country is in the high-risk list, else 'OK'."""
    if country in high_risk_list:
        return "FLAGGED: high-risk country"
    return "OK"
