import pytest
from app.calculations import BankAccount, add

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