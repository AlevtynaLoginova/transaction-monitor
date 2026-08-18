from monitor import flag_large_transaction, flag_velocity

def test_under_threshold():
    assert flag_large_transaction(500) == "OK"

def test_at_threshold():
    assert flag_large_transaction(10000) == "FLAGGED: large transaction"

def test_over_threshold():
    assert flag_large_transaction(25000) == "FLAGGED: large transaction"

def test_high_velocity():
    assert flag_velocity([0, 2, 4, 5]) == "FLAGGED: high velocity"



