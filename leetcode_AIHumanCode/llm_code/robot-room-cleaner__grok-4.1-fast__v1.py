class Solution:
    def cleanRoom(self, robot):
        def backtrack(row, col, drow, dcol, visited):
            robot.clean()
            visited.add((row, col))
            for _ in range(4):
                next_row = row + drow
                next_col = col + dcol
                if (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    if robot.move():
                        backtrack(next_row, next_col, drow, dcol, visited)
                        robot.turnRight()
                        robot.turnRight()
                        robot.move()
                        robot.turnLeft()
                        robot.turnLeft()
                robot.turnRight()
                drow, dcol = dcol, -drow
        
        backtrack(0, 0, 0, 1, robot, set())
