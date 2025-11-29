from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        targets = defaultdict(list)
        for src, dst in tickets:
            targets[src].append(dst)
        for neighbors in targets.values():
            neighbors.sort(reverse=True)
        itinerary = []
        route = ["JFK"]
        while route:
            city = route[-1]
            if targets[city]:
                route.append(targets[city].pop())
            else:
                itinerary.append(route.pop())
        itinerary.reverse()
        return itinerary
