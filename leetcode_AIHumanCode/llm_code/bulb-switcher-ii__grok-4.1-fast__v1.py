class Solution:
    def flipLights(self, bulbs, flips):
        if flips == 0:
            return 1
        if bulbs == 1:
            return 2
        if flips == 1:
            return 3 if bulbs == 2 else 4
        if bulbs == 2 or flips == 2:
            return 4 if bulbs == 2 else 7
        return 8
