from datetime import date
class BankAccount:
    def __init__(self,initial_amount):
        self._balance = initial_amount
        self._deposits = []
        self.opendate = date(2011,3,15)
    def makeDeposit(self,amount):
        self._balance += amount
        self._deposits.append(amount)
    def makeWithdrawal(self,amount):
        self._balance -= amount
    def getBalance(self):
        return self._balance
    def getDeposits(self):
        copied_list = self._deposits[:]
        return copied_list
    def __str__(self):
        deposits_str = ""
        for i in range(len(self._deposits)):
            deposits_str +='deposit N :'+str(i)+' is '+ str(self._deposits[i])+" "
        return deposits_str

#play with properties and methods
my_account = BankAccount(1000)
my_account.makeDeposit(500)
my_account.makeDeposit(500)
my_account.makeWithdrawal(200)
# need to watch out for using mutable data as it can affect our properties example below with lists for deposits
x = my_account.getDeposits()
x.append(1000)
y= my_account.getBalance()
y += 100


def winLottery(account):
    account.makeDeposit(1000000)
winLottery(my_account)


print(my_account.getBalance())
print(my_account)
print(my_account.opendate)