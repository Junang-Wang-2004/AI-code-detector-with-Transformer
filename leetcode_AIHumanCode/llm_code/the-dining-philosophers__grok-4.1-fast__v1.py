import threading

class DiningPhilosophers:
    def __init__(self):
        self.fork_locks = [threading.Lock() for _ in range(5)]

    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        left_fork = philosopher
        right_fork = (philosopher + 4) % 5
        smaller = min(left_fork, right_fork)
        larger = max(left_fork, right_fork)
        with self.fork_locks[smaller]:
            with self.fork_locks[larger]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
