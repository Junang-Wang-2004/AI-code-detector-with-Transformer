class C1:

    def __init__(self, a1):
        self.num_accounts = len(a1)
        self.funds = a1

    def deposit(self, a1, a2):
        v1 = a1 - 1
        if 0 <= v1 < self.num_accounts:
            self.funds[v1] += a2
            return True
        return False

    def withdraw(self, a1, a2):
        v1 = a1 - 1
        if 0 <= v1 < self.num_accounts and self.funds[v1] >= a2:
            self.funds[v1] -= a2
            return True
        return False

    def transfer(self, a1, a2, a3):
        v1 = a1 - 1
        v2 = a2 - 1
        if 0 <= v1 < self.num_accounts and 0 <= v2 < self.num_accounts and (self.funds[v1] >= a3):
            self.funds[v1] -= a3
            self.funds[v2] += a3
            return True
        return False
