class MyCalendarThree:
    def __init__(self):
        self.changes = []

    def book(self, begin, finish):
        self.changes.append((begin, 1))
        self.changes.append((finish, -1))
        self.changes.sort(key=lambda p: (p[0], p[1]))
        active = 0
        highest = 0
        for _, delta in self.changes:
            active += delta
            if active > highest:
                highest = active
        return highest
