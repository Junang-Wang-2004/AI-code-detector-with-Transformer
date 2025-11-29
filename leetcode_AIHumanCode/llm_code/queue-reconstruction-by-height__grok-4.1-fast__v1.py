class Solution:
    def reconstructQueue(self, people):
        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
        queue = []
        for person in sorted_people:
            queue.insert(person[1], person)
        return queue
