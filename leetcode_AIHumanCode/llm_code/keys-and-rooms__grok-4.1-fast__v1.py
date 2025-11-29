class Solution:
    def canVisitAllRooms(self, rooms):
        visited = set()
        def traverse(idx):
            visited.add(idx)
            for adj in rooms[idx]:
                if adj not in visited:
                    traverse(adj)
        traverse(0)
        return len(visited) == len(rooms)
