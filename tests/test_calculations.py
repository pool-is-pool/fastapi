import pytest
from app.calculations import BankAccount, add, InsufficientFunds

@pytest.mark.parametrize("num1, num2, expected", [
    (3,2,5),
    (4,5,9),
    (34,45,79)
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected

def test_bank_set_initial_amount():
    bank_account = BankAccount(50)
    assert bank_account.balance == 50

def test_bank_default_initial_amount():
    bank_account = BankAccount(0)
    assert bank_account.balance == 0

def test_withdraw():
    bank_account = BankAccount(50)
    bank_account.withdraw(30)
    assert bank_account.balance == 20

def test_withdraw():
    bank_account = BankAccount(50)
    bank_account.deposit(30)
    assert bank_account.balance == 80

def test_collect_interest():
    bank_account = BankAccount(50)
    bank_account.collect_interest()
    assert round(bank_account.balance, 2) == 55


@pytest.mark.parametrize("deposited, withdrew, expected", [
    (300,200,100),
    (4000,400,3600),
    (33,22,11)
])
def test_bank_transaction(deposited, withdrew, expected):
    bank_account = BankAccount()
    bank_account.deposit(deposited)
    bank_account.withdraw(withdrew)
    assert bank_account.balance == expected

def test_insufficient_funds():
    bank_account = BankAccount(50)
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(100)