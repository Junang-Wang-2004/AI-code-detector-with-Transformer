class C1(object):

    def __init__(self, a1):
        """
        """
        self.__balance = a1

    def transfer(self, a1, a2, a3):
        """
        """
        if 1 <= a2 <= len(self.__balance) and self.withdraw(a1, a3):
            return self.deposit(a2, a3)
        return False

    def deposit(self, a1, a2):
        """
        """
        if 1 <= a1 <= len(self.__balance):
            self.__balance[a1 - 1] += a2
            return True
        return False

    def withdraw(self, a1, a2):
        """
        """
        if 1 <= a1 <= len(self.__balance) and self.__balance[a1 - 1] >= a2:
            self.__balance[a1 - 1] -= a2
            return True
        return False
