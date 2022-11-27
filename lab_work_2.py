# def question_1(a, b):
#     if a%2==0:
#         while a <= b:
#             print(a, end=" ")
#             a+=2
#     else:
#         while a < b:
#             print(a+1, end=" ")
#             a+=2
#
# a = int(input("Enter the a "))
# b = int(input("Enter the b "))
# question_1(a, b)

# def question_2(x):
#     for i in range(2,x+1):
#         if x%i==0:
#             print(i)
#             break
#
# x = int(input("Enter the x "))
# question_2(x)

# def question_3(x):
#     for i in range(1,x+1):
#         if x%i==0:
#             print(i, end=" ")
#
# x = int(input("Enter the x "))
# question_3(x)

# def question_4(N):
#     sum = 0
#     for i in range(N):
#         sum+=int(input(f"Enter the number {i+1} "))
#     print(sum)
#
# N = int(input("Enter the N value "))
# question_4(N)

# def question_5(binary_num):
#     ten_digit = 0
#     l = len(binary_num) - 1
#     for i in binary_num:
#         i = int(i)
#         ten_digit += i*(2**l)
#         l-=1
#     print(ten_digit)
#
# binary_num = str(input("Enter the value "))
# question_5(binary_num)

# def question_6(a: float, n: int):
#     power = 1
#     for i in range(n):
#         power*=a
#     print(power)
#
# a, n = input().split()
# a, n = float(a), int(n)
# question_6(a, n)

# def question_7(x:bool, y:bool, z:bool):
#     if int(x)+int(y)+int(z) >= 2:
#         print(1)
#     else:
#         print(0)
#
# x, y, z = input("Enter the bool values ").split()
# question_7(x, y, z)

account_balance = 200
currency = 'KZT'
def addToBackAccount(x, account_balance):
    account_balance+=x
    print(f'You add {x} {currency} to your account and current balance is {account_balance} {currency}')

x = 50
addToBackAccount(x, account_balance)

def substractFromBankAccount(x, account_balance):
    account_balance-=x
    print(f'You withdraw {x} {currency} from your account and current balance is {account_balance} {currency}')

substractFromBankAccount(100, account_balance)

def moneyConversion(account_balance, currency):
    if currency == "KZT":
        account_balance/=470
        currency_new = "USD"
    else:
        account_balance*=470
        currency_new = "KZT"
    currency = currency_new
    print(f"You convert to {currency} and new balance is {round(account_balance,2)} {currency}")

moneyConversion(account_balance, currency)



