# Write your code here
import random
import dataserver
import sqlite3

class BankMenu:
    account = {}
    def __init__(self):
        a = dataserver.data_server(random.randint(0,9),1, 1)
        a.select_op('create')
    def menu(self):
        while True:
            command = input('''1. Create an account
        2. Log into account
        0. Exit''').strip()
            if command == '0':
                print('\nBye!')
                exit()
            elif command == '1':
                self.create_account()
            elif command == '2':
                self.login_account()
            else:
                print("Invalid input")

    def create_account(self):
        print('Your card has been created')
        card_nO = self.generate_cardnO()
        card_PIN = ''.join([str(random.randint(0,9)) for i in range (4)])
        self.account[card_nO] = card_PIN
        print('Your card number:')
        print(card_nO)
        print('Your card PIN:')
        print(card_PIN)
        a = dataserver.data_server(random.randint(0,9),card_nO, card_PIN)
        a.select_op('insert')

    def generate_cardnO(self):
        card_nO = []
        card_res = []
        for i in range(9):
            card_nO.append(random.randint(0,9))
            card_res.append(card_nO[i])
        sum_nO = 8
        for index in range(len(card_nO)):
            if index % 2 == 0:
                card_nO[index] = card_nO[index]*2
                if card_nO[index] > 9:
                    card_nO[index] = card_nO[index]-9
            sum_nO += card_nO[index]
        if sum_nO % 10 == 0:
            checksum = 0
        else:
            checksum = 10 - sum_nO%10
        card_new = '400000'+''.join(str(e) for e in card_res)+''.join(str(checksum))
        return card_new


    def login_account(self):
        card_nO = input('Enter your card number:')
        card_PIN = input('Enter your PIN:')
        if card_nO in self.account and self.account[card_nO] == card_PIN:
            print('You have successfully logged in!')
            session_id = random.randint(1,100)
            self.choice_menu(session_id, card_nO, card_PIN)
        else:
            print('Wrong card number or PIN\n')

    def choice_menu(self, session_id, card_nO, card_PIN):
        a = dataserver.data_server(session_id,card_nO, card_PIN)
        while True:
            choice = input('''
            1. Balance
            2. Add income
            3. Do transfer
            4. Close account
            5. Log out
            0. Exit''').strip()
            if choice == '1':
                a.select_op('balance')
            elif choice == '2':
                a.select_op('add_income')
            elif choice == '3':
                a.select_op('transfer')
            elif choice == '4':
                a.select_op('close_account')
            elif choice == '5':
                print('You have successfully logged out!')
                return
            elif choice == '0':
                a.select_op('delete')
                print('Bye!')
                exit()
            else:
                print("Invalid input")


a = BankMenu()
a.menu()


