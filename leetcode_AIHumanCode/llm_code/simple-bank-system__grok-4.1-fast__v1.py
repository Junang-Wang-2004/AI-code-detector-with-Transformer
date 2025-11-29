class Bank:
    def __init__(self, balance):
        self.num_accounts = len(balance)
        self.funds = balance

    def deposit(self, account, amount):
        i = account - 1
        if 0 <= i < self.num_accounts:
            self.funds[i] += amount
            return True
        return False

    def withdraw(self, account, amount):
        i = account - 1
        if 0 <= i < self.num_accounts and self.funds[i] >= amount:
            self.funds[i] -= amount
            return True
        return False

    def transfer(self, source, target, amount):
        s = source - 1
        t = target - 1
        if (0 <= s < self.num_accounts and
            0 <= t < self.num_accounts and
            self.funds[s] >= amount):
            self.funds[s] -= amount
            self.funds[t] += amount
            return True
        return False
