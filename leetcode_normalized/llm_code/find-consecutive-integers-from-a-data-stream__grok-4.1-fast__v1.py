class C1:

    def __init__(self, a1, a2):
        self.target = a1
        self.min_consec = a2
        self.streak = 0

    def consec(self, a1):
        self.streak = self.streak + 1 if a1 == self.target else 0
        return self.streak >= self.min_consec
