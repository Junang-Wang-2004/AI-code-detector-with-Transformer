from collections import defaultdict
from sortedcontainers import SortedList


class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.foodCuisine = dict(zip(foods, cuisines))
        self.foodRating = dict(zip(foods, ratings))
        self.cuisineFoods = defaultdict(SortedList)
        for f in foods:
            c = self.foodCuisine[f]
            r = self.foodRating[f]
            self.cuisineFoods[c].add((-r, f))

    def changeRating(self, food, newRating):
        c = self.foodCuisine[food]
        prevRating = self.foodRating[food]
        self.cuisineFoods[c].remove((-prevRating, food))
        self.foodRating[food] = newRating
        self.cuisineFoods[c].add((-newRating, food))

    def highestRated(self, cuisine):
        return self.cuisineFoods[cuisine][0][1]
