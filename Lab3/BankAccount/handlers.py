import decimal
from typing import Optional

from BankAccount.models import BankAccount, AccountType
from BankAccount.services import BankAccountServices


class BankAccountHandlers:

    services: BankAccountServices

    def __init__(self, services: BankAccountServices):
        self.services = services

    def sign_up(self, name: str, surname: str, account_type: AccountType) -> None:
        name = name.strip()
        surname = surname.strip()
        account = decimal.Decimal(0)
        account_type = account_type

        if not self._validate_bank_account(name, surname, account, account_type):
            print("Please enter the correct values")
            return None

        self.services.create_bank_account(name=name, surname=surname, account=account, account_type=account_type)

    def sign_in(self, name: str) -> Optional[BankAccount]:
        name = name.strip()
        return self.services.get_bank_account(name=name)

    def addToBankAccount(self, user: BankAccount, add: str):
        add = decimal.Decimal(add)
        account_type = user.account_type
        self.services.set_account(user=user, account=add, account_type=account_type)

    def subtractFromBankAccount(self, user: BankAccount, add: str):
        add = decimal.Decimal(add)*-1
        account_type = user.account_type
        self.services.set_account(user=user, account=add, account_type=account_type)

    def moneyConversion(self, user: BankAccount, new_currency: AccountType):
        new_account = user.account
        if user.account_type == AccountType.KZT:
            if new_currency == AccountType.USD:
                new_account = new_account/468
            elif new_currency == AccountType.RUB:
                new_account = new_account/ 6
            elif new_currency == AccountType.EUR:
                new_account = new_account/496
            elif new_currency == AccountType.KZT:
                new_account = new_account
        elif user.account_type == AccountType.RUB:
            if new_currency == AccountType.USD:
                new_account = new_account/65
            elif new_currency == AccountType.RUB:
                new_account = new_account
            elif new_currency == AccountType.EUR:
                new_account = new_account/69
            elif new_currency == AccountType.KZT:
                new_account = new_account*6
        elif user.account_type == AccountType.USD:
            if new_currency == AccountType.USD:
                new_account = new_account
            elif new_currency == AccountType.RUB:
                new_account = new_account*65
            elif new_currency == AccountType.EUR:
                new_account = new_account/1.06
            elif new_currency == AccountType.KZT:
                new_account = new_account*468
        elif user.account_type == AccountType.EUR:
            if new_currency == AccountType.USD:
                new_account = new_account*1.06
            elif new_currency == AccountType.RUB:
                new_account = new_account*69
            elif new_currency == AccountType.EUR:
                new_account = new_account
            elif new_currency == AccountType.KZT:
                new_account = new_account*496
        new_account = new_account - user.account
        self.services.set_account(user=user, account=new_account, account_type=new_currency)

    def Tostring(self, bank_account: BankAccount):
        account = bank_account.account
        print(f"You current amount is {account}")

    @staticmethod
    def _validate_bank_account(name: str, surname: str, account: decimal.Decimal, account_type: AccountType) -> bool:


        if type(account_type) != AccountType:
            print("The account_type should be UZD, RUB, KZT or EUR ")
            return False

        return True
