import decimal
from typing import Optional

from BankAccount.models import BankAccount, AccountType
from BankAccount.repositories import BankAccountRepositories


class BankAccountServices:

    repositories: BankAccountRepositories

    def __init__(self, repositories: BankAccountRepositories):
        self.repositories = repositories

    def create_bank_account(self, name: str, surname: str, account: decimal.Decimal, account_type: BankAccount) -> None:
        self.repositories.create_bank_account(name=name, surname=surname, account=account, account_type=account_type)

    def get_bank_account(self, name: str) -> Optional[BankAccount]:
        return self.repositories.get_bank_account(name=name)

    def set_account(self, user: BankAccount, account: decimal.Decimal, account_type: AccountType) -> None:
        self.repositories.set_account(user=user, account=account, account_type=account_type)
