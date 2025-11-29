import heapq

class SeatManager:

    def __init__(self, n: int):
        self.free_seats = [seat_num for seat_num in range(1, n + 1)]
        heapq.heapify(self.free_seats)

    def reserve(self) -> int:
        return heapq.heappop(self.free_seats)

    def unreserve(self, seat_id: int) -> None:
        heapq.heappush(self.free_seats, seat_id)
