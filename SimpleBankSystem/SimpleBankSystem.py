import unittest


class Bank:
    def __init__(self, balance: list[int]):
        self.balance = balance

    def transfer(self, acc1: int, acc2: int, money: int) -> bool:
        try:
            if self.balance[acc1-1] >= money and self.balance[acc2-1] >= 0:
                self.balance[acc1-1] -= money
                self.balance[acc2-1] += money
                return True
            else:
                return False
        except:
            return False

    def deposit(self, acc: int, money: int) -> bool:
        try:
            self.balance[acc-1] += money
            return True
        except:
            return False
        
    def withdraw(self, acc: int, money: int) -> bool:
        try:
            if self.balance[acc-1] >= money:
                self.balance[acc-1] -= money
                return True
            else:
                return False
        except:
            return False
        
class TestSimpleBankSystem(unittest.TestCase):
    def test_simple_bank_system_success(self):
        A = Bank([])
        actual = [A.__init__([10, 100, 20, 50, 30]), A.withdraw(3, 10), A.transfer(5, 1, 20), A.deposit(5, 20), A.transfer(3, 4, 15), A.withdraw(10, 50)]
        expected = [None, True, True, True, False, False]
        self.assertEqual(actual,expected)

unittest.main()
#A = Bank([10, 100, 20, 50, 30])
#A.withdraw(3, 10)
#A.transfer(5, 1, 20)
#A.deposit(5, 20)
#A.transfer(3, 4, 15)
#A.withdraw(10, 50)

#print(A)
