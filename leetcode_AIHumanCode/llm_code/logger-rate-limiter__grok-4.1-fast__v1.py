import collections

class Logger:
    def __init__(self):
        self.q = collections.deque()
        self.seen = set()

    def cleanup(self, t):
        while self.q and self.q[0][0] <= t - 10:
            time, msg = self.q.popleft()
            self.seen.remove(msg)

    def shouldPrintMessage(self, timestamp, message):
        self.cleanup(timestamp)
        if message in self.seen:
            return False
        self.q.append((timestamp, message))
        self.seen.add(message)
        return True
