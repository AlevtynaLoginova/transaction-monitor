from sanctions import flag_sanctioned_country, flag_high_risk_country

from monitor import flag_large_transaction, flag_velocity

def test_under_threshold():
    assert flag_large_transaction(500) == "OK"

def test_at_threshold():
    assert flag_large_transaction(10000) == "FLAGGED: large transaction"

def test_over_threshold():
    assert flag_large_transaction(25000) == "FLAGGED: large transaction"

def test_high_velocity():
    assert flag_velocity([0, 2, 4, 5]) == "FLAGGED: high velocity"

def test_sanctioned_country ():
    assert flag_sanctioned_country ("Iran") == "FLAGGED: Sanctioned country"

def test_high_risk_country ():
    asser flag_high_risk_country ("Nigeria") == "FLAGGED: high-risk country"

