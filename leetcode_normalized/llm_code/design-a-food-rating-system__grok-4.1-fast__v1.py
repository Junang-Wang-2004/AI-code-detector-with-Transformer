from collections import defaultdict
from sortedcontainers import SortedList

class C1:

    def __init__(self, a1, a2, a3):
        self.foodCuisine = dict(zip(a1, a2))
        self.foodRating = dict(zip(a1, a3))
        self.cuisineFoods = defaultdict(SortedList)
        for v1 in a1:
            v2 = self.foodCuisine[v1]
            v3 = self.foodRating[v1]
            self.cuisineFoods[v2].add((-v3, v1))

    def changeRating(self, a1, a2):
        v1 = self.foodCuisine[a1]
        v2 = self.foodRating[a1]
        self.cuisineFoods[v1].remove((-v2, a1))
        self.foodRating[a1] = a2
        self.cuisineFoods[v1].add((-a2, a1))

    def highestRated(self, a1):
        return self.cuisineFoods[a1][0][1]
