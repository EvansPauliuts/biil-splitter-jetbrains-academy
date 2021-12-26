# write your code here
import random


class BillArrived:

    def __init__(self):
        self.num = 0
        self.total = 0
        self.data = {}
        self.name = ''
        self.question_text = ''

    def create_num_joining(self):
        print('Enter the number of friends joining (including you):')
        num_join = int(input())
        self.num = num_join

    def create_every_friend(self):
        print('Enter the name of every friend (including you), each on a new line:')
        for _ in range(self.num):
            name_in = input()
            d = {name_in: self.num}
            self.data.update(d)

    def total_bill(self):
        print()
        print('Enter the total bill value:')
        num_total = int(input())
        print()
        self.total = num_total

    def for_key_name(self, name):
        find_jem_num = self.data.get(name)
        tst_num = round(find_jem_num / (self.num - 1), 2)

        for key, value in self.data.items():
            if key == name:
                self.data.update({name: 0})
            else:
                self.data.update({key: value + tst_num})

    def question_write(self):
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        question = input()
        print()
        self.question_text = question

        if question != 'No':
            print(f'{self.name} is the lucky one!')
        else:
            print('No one is going to be lucky')
        print()

    def info_valid(self):
        try:
            if self.num > 0:
                self.create_every_friend()
                self.total_bill()

                for key, value in self.data.items():
                    result_sum = round(self.total / value, 2)
                    data = {key: result_sum}
                    self.data.update(data)

                key = random.choice(list(self.data))
                self.name = key

                self.question_write()

                if self.question_text == 'Yes':
                    self.for_key_name(key)
                    print(self.data)
                else:
                    print(self.data)
            else:
                print('No one is joining for the party')
        except ZeroDivisionError:
            print('No one is joining for the party')

    def __repr__(self):
        return f'{self.data}'


bill = BillArrived()
bill.create_num_joining()
print()
bill.info_valid()
