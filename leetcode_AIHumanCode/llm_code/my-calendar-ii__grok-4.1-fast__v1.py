class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.doubles = []

    def book(self, left, right):
        for dl, dr in self.doubles:
            if max(left, dl) < min(right, dr):
                return False
        for el, er in self.events:
            ol = max(left, el)
            oor = min(right, er)
            if ol < oor:
                self.doubles.append((ol, oor))
        self.events.append((left, right))
        return True
