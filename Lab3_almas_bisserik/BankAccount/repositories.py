import decimal
from typing import List, Optional
from BankAccount.models import BankAccount, AccountType


class BankAccountRepositories:
    bank_accounts: List[BankAccount] = []


    def create_bank_account(self, name: str, surname: str, account: decimal.Decimal, account_type: AccountType) -> None:
        bank_account = BankAccount(name=name, surname=surname, account=account, account_type=account_type)
        self.bank_accounts.append(bank_account)

    def get_bank_account(self, name: str) -> Optional[BankAccount]:
        name = next(
            (ac for ac in self.bank_accounts if name == ac.name),
            None
        )

        if not name:
            print('BankAccount not found')
            return

        return name
    def set_account(self, user:BankAccount, account: decimal.Decimal, account_type: AccountType):
        user.account+=account
        user.account_type=account_type

