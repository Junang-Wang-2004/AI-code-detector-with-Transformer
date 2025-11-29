import threading


class FizzBuzz:
    def __init__(self, n):
        self.maxn = n
        self.status = 0
        self.sync = threading.Condition()

    def _step(self, my_turn, check, prnt):
        for val in range(1, self.maxn + 1):
            with self.sync:
                while self.status != my_turn:
                    self.sync.wait()
                self.status = (self.status + 1) % 4
                if check(val):
                    prnt()
                self.sync.notify_all()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        """
        self._step(0, lambda x: x % 3 == 0 and x % 5 != 0, printFizz)

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        """
        self._step(1, lambda x: x % 5 == 0 and x % 3 != 0, printBuzz)

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        """
        self._step(2, lambda x: x % 3 == 0 and x % 5 == 0, printFizzBuzz)

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        """
        self._step(3, lambda x: x % 3 != 0 and x % 5 != 0, printNumber)
