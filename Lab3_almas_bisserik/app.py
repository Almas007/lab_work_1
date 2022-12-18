import sys

from BankAccount.handlers import BankAccountHandlers
from BankAccount.repositories import BankAccountRepositories
from BankAccount.services import BankAccountServices
from BankAccount.models import AccountType, BankAccount


def init():
    bank_account_repositories = BankAccountRepositories()
    bank_account_services = BankAccountServices(repositories=bank_account_repositories)
    bank_account_handlers = BankAccountHandlers(services=bank_account_services)
    bankAccount: BankAccount
    while True:
        command = input('Enter command \n'
                        '1 - sign up \n'
                        '2 - sign in \n'
                        'q (quit) to exit: \n')

        if command == 'q':
            sys.exit(0)

        if command == '1':
            name = input("Please enter your name ")
            surname = input("Please enter your surname ")
            account_type = input("Please enter the currency you want to use (USD, RUB, KZT, EUR) ")
            if account_type=="USD":
                account_type = AccountType.USD
            elif account_type=="RUB":
                account_type = AccountType.RUB
            elif account_type=="KZT":
                account_type = AccountType.KZT
            elif account_type=="EUR":
                account_type = AccountType.EUR
            else:
                print("Please check your Entered currency")
            bank_account_handlers.sign_up(name=name, surname=surname, account_type=account_type)
        elif command == '2':
            name = input('Please, enter your name: ')
            bankAccount = bank_account_handlers.sign_in(name=name)
            if bankAccount != None:
                while True:
                    command2 = input("What you want to do \n "
                                     "1 - Check your current account? \n "
                                     "2 - add to bank account \n "
                                     "3 - Subtract from bank account \n"
                                     "4 - Convert account \n"
                                     "q - sign out \n")
                    if command2 == "1":
                        bank_account_handlers.Tostring(bankAccount)
                    elif command2 == "2":
                        bank_account_handlers.addToBankAccount(user=bankAccount, add=input("Please enter amount you want to add "))
                        bank_account_handlers.Tostring(bankAccount)
                    elif command2 == "3":
                        bank_account_handlers.subtractFromBankAccount(user=bankAccount, add=input("Please enter amount you want to substract "))
                        bank_account_handlers.Tostring(bankAccount)
                    elif command2 == '4':
                        new_currency: AccountType
                        if bankAccount.account == 0:
                            print("You balance is null, conversion is not possible")
                            return
                        input_check = input("Please choose which currency you want to change to \n"
                                             "1 - USD \n"
                                             "2 - EUR \n"
                                             "3 - RUB \n"
                                             "4 - KZT \n")
                        if input_check == "1":
                            new_currency = AccountType.USD
                        elif input_check == "2":
                            new_currency = AccountType.EUR
                        elif input_check == "3":
                            new_currency = AccountType.RUB
                        elif input_check == '4':
                            new_currency = AccountType.KZT
                        else:
                            "Please enter the number from 1 to 4 related with currency"
                        bank_account_handlers.moneyConversion(user=bankAccount, new_currency=new_currency)
                        bank_account_handlers.Tostring(bankAccount)
                    elif command2=="q":
                        sys.exit(0)
        else:
            print('invalid command, try again')


if __name__ == '__main__':
    init()
