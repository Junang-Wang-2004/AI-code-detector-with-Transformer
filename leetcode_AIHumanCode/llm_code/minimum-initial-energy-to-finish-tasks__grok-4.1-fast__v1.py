class Solution:
    def minimumEffort(self, tasks):
        ordered = sorted(tasks, key=lambda t: t[1] - t[0])
        energy = 0
        for cost, req in ordered:
            energy = max(energy + cost, req)
        return energy
