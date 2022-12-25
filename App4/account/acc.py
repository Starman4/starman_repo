class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open (filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance-amount

    def deposit(self, amount):
        self.balance=self.balance+amount

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """this class generates checking account objects"""

    type="checking"

    def __init__(self,filepath,fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self,amount):
        self.balance=self.balance-amount-self.fee

jacks_checking=Checking("jack.txt",1)
jacks_checking.transfer(100)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)

bobs_checking=Checking("bob.txt",1)
bobs_checking.transfer(100)
print(bobs_checking.balance)
bobs_checking.commit()
