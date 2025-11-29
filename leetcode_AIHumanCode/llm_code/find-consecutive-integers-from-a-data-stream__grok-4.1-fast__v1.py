class DataStream:

    def __init__(self, value, k):
        self.target = value
        self.min_consec = k
        self.streak = 0

    def consec(self, num):
        self.streak = self.streak + 1 if num == self.target else 0
        return self.streak >= self.min_consec
