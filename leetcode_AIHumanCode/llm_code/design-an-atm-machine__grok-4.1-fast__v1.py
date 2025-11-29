class ATM:

    def __init__(self):
        self.denominations = [20, 50, 100, 200, 500]
        self.available = [0] * 5

    def deposit(self, note_counts):
        for index, quantity in enumerate(note_counts):
            self.available[index] += quantity

    def withdraw(self, requested):
        counts_to_use = [0] * 5
        balance = requested
        for position in range(4, -1, -1):
            note_value = self.denominations[position]
            take = min(balance // note_value, self.available[position])
            counts_to_use[position] = take
            balance -= take * note_value
        if balance != 0:
            return [-1]
        for position in range(5):
            self.available[position] -= counts_to_use[position]
        return counts_to_use
