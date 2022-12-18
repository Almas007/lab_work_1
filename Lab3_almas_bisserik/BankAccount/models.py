import decimal
from enum import Enum

class AccountType(Enum):
    KZT = 'KZT'
    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'

class BankAccount:
    name: str
    surname: str
    account: decimal.Decimal
    account_type: AccountType

    def __init__(self, name: str, surname:str, account: decimal.Decimal, account_type: AccountType):
        self.name = name
        self.surname = surname
        self.account = account
        self.account_type = account_type
    def __del__(self):
        print("Bank Account is deleted")


