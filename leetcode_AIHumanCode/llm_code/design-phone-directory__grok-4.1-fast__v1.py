class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        self._avail = set(range(maxNumbers))
        self._size = maxNumbers

    def get(self):
        if self._avail:
            return self._avail.pop()
        return -1

    def check(self, number):
        return 0 <= number < self._size and number in self._avail

    def release(self, number):
        if 0 <= number < self._size and number not in self._avail:
            self._avail.add(number)
