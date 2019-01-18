'''
Author: Robin Nguyen
Date: 1/18/2019
Program and purpose:
    Python program created via Visual Studios. The purpose of this program is to 
    allow the user to operate within the bank of Narnia. The user will be able to
    do the typical operations that an ATM would allow one to do such as deposit, 
    withdraw, check balanace, etc.
'''

class Account():

    def __init__(self,owner,balance=0):
        
        self.owner=owner
        self.balance=balance

        print(f"Welcome to the bank of Narnia, {self.owner}!\nYour current balance is: ${self.balance}")

    def deposit(self,dep_amt):

        self.balance=self.balance+dep_amt
        print("Deposited {} to the balance".format(dep_amt))

    def withdrawal(self,wd_amt):

        if self.balance >= wd_amt:
            self.balance=self.balance-wd_amt
            print("Withdrawal accepted")
        else:
            print("Sorry, not enough funds!")

    def __str__(self):
        return f"Owner: {self.owner}\nBalance: {self.balance}"

def print_options():
# List of options from menu ( View balance, withdraw, deposit, or exit )
    print('B to view Balance.')
    print('W to withdraw.')
    print('D to deposit.')
    print('Q to exit.')

def print_options():
# List of options from menu ( View balance, withdraw, deposit, or exit )
    print('B to view Balance.')
    print('W to withdraw.')
    print('D to deposit.')
    print('Q to exit.')

a=Account("Robin",476)
response=''
while(response!='q'):
    print_options()
    response=input('User choice: ').lower()
    if response=='b':
        print("Current Balance: ${}".format(a.balance))
    elif response=='w':
        withdrawal_amount=int(input('How much would you like to withdrawal?\n'))
        a.withdrawal(withdrawal_amount)
    elif response=='d':
        depo_amt=int(input('How much would you like to deposit?\n'))
        a.deposit(depo_amt)
    elif response=='q':
        print("HASTA LUEGO!")
    else:
        print("Wrong response")
