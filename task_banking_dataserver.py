import sqlite3

class data_server:
    def __init__(self,id, number, pin):
        self.id = id
        self.number = number
        self.pin = pin
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.select_op('create')
        self.balance = 0

    def select_op(self, command):
        if command == 'insert':
            query = 'INSERT INTO card VALUES(?,?,?,?)'
            data_tuple = (self.id, self.number, self.pin, 0)
            self.cur.execute(query, data_tuple)
            self.conn.commit()
        elif command == 'balance':
            query = 'SELECT balance FROM card WHERE number = ? and pin = ?'
            data_tuple = (self.number, self.pin)
            self.cur.execute(query, data_tuple)
            row = self.cur.fetchone()
            self.balance = row[0]
            print('Balance: ',self.balance)

        elif command == 'add_income':
            income = int(input('Enter income'))
            self.balance += income
            query = 'UPDATE card SET balance = ? where number = ? and pin = ?'
            data_tuple = (self.balance, self.number, self.pin)
            self.cur.execute(query, data_tuple)
            self.conn.commit()
            print('Income was added!')

        elif command == 'transfer':
            dest_card = input('Enter card number:')
            if self.check_validate(dest_card) == False:
                print('Probably you made a mistake in the card number. Please try again!')
                return
            if self.search_client(dest_card) == 1:
                print("Such a card does not exist")
                return
            if dest_card == self.number:
                print("You can't transfer money to the same account!")
                return
            trans_money = int(input('Enter how much money you want to transfer:'))
            out_ = self.balance - trans_money
            if out_ < 0:
                print('Not enough money!')
                return
            query_out = 'UPDATE card SET balance = ? where number = ? and pin = ?'
            query_in = 'UPDATE card SET balance = ? where number = ?'
            dest_balance = self.search_client(dest_card)
            in_ = dest_balance + trans_money
            data_tuple_out = (out_, self.number, self.pin)
            data_tuple_in = (in_, dest_card)
            self.cur.execute(query_out, data_tuple_out)
            self.cur.execute(query_in, data_tuple_in)
            self.conn.commit()
            self.balance -= out_
            print('Success!')
        elif command == 'close_account':
            query = 'DELETE FROM card WHERE number = ? and pin = ?'
            data_tuple = (self.number, self.pin)
            self.cur.execute(query, data_tuple)
            self.conn.commit()
            print("The account has been closed!")
            return

        elif command == 'create':
            query = '''CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT,
        pin TEXT, balance INTEGER DEFAULT 0);'''
            self.cur.execute(query)
            self.conn.commit()
        else:
            print("Invaild Command")

    def search_client(self, card_nO):
        query = "SELECT balance FROM card WHERE number = ? "
        self.cur.execute(query, (card_nO,))
        row = self.cur.fetchone()
        if row:
            return row[0]
        else:
            return 1

    def check_validate(self, card_nO):
        sum_nO = 0
        card_new = []
        for i in card_nO:
            card_new.append(int(i))
        for index in range(len(card_nO)-1):
            if index % 2 == 0:
                card_new[index] = card_new[index]*2
                if card_new[index] > 9:
                    card_new[index] = card_new[index]-9
            sum_nO += card_new[index]
        sum_nO += card_new[-1]
        if sum_nO % 10 == 0:
            return True
        else:
            return False
