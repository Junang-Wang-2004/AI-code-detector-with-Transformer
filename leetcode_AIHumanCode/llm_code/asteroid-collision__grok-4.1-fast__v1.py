class Solution(object):
    def asteroidCollision(self, asteroids):
        survivors = []
        for rock in asteroids:
            blow_up = False
            while survivors and survivors[-1] > 0 and rock < 0:
                prev = survivors[-1]
                if prev < -rock:
                    survivors.pop()
                else:
                    if prev == -rock:
                        survivors.pop()
                    blow_up = True
                    break
            if not blow_up:
                survivors.append(rock)
        return survivors
