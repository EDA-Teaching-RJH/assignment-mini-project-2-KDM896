import importlib
import pytest


module = importlib.import_module("prodject")

def test_maths_logic():

    start = 5500
    test_transactions = [
        module.Income("2026-03-28", 1000, "Salary", "Work"),
        module.Expenses("2026-03-28", 500, "Food", "Co-op")
    ]
    result = module.calculate_balance(start, test_transactions)
    assert result == 6000, f"Expected 6000 but got {result}"# 

def test_empty_list():
    assert module.calculate_balance(5500, []) == 5500

def test_security_check():
    assert module.check_credentials("Kenzie Minott", "14-01-2006", "7890") == True
    assert module.check_credentials("Wrong Name", "14-01-2006", "7890") == False
    assert module.check_credentials("Kenzie Minott", "Wrong Date", "7890") == False
    assert module.check_credentials("Kenzie Minott", "14-01-2006", "Wrong Passcode") == False