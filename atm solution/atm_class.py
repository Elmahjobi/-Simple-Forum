from time import ctime, sleep
from collections import namedtuple

class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawal_tuple = namedtuple( 'withdrawal','value date' )
        self.withdrawal_list = []

    def _line(self):
        print "="*30

    def _show_withdrawals(self):
        for record in self.withdrawal_list:
            print str( record.value ) + "$ withdrawn at " + record.date

    def withdraw(self,request):
        paper_values = [ 100, 50, 10, 5, 1]

        self._line()
        print "Welcome to " + self.bank_name +" !"
        print "Current Balance: "+ str(self.balance)

        if request <= 0 :
            print "Invalid input !" ;
        elif request > self.balance :
            print "Balance Not Enough !" ;
        else:
            self.withdrawal_list.append( self.withdrawal_tuple( request, ctime() ) )
            self.balance -= request
            print "Delivering " + str(request) + "$ to client:"
            for x in paper_values:
                while request >= x:
                    print "give" + str(x)
                    request -= x
            print "Remaining balance " + str( self.balance )
        self._line()
        return self.balance

#making objects of type ATM
atm1 = ATM( 500, "AMAN BANK")

#testing withdraw method for those objects
atm1.balance = atm1.withdraw(50)
sleep(5)
atm1.balance = atm1.withdraw(150)
atm1._show_withdrawals()
