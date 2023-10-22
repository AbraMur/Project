from constant import *

class Grid_visual(object):
    def __init__(self, position, heights):
        self.position = position
        self.heights = heights
        self.size = len(heights) // zoom - 1

    def transform(self):
        heights_n = [[0 for i in range(len(self.heights))] for j in range(len(self.heights))]
        position = ((len(self.heights) - (self.size // 2 - 1) * 2) // 2) + self.position[0], \
                   ((len(self.heights) - (self.size // 2 - 1) * 2) // 2) + self.position[1]
        print(position, self.size)

        for x in range(position[0], position[0] + self.size):
            for y in range(position[1], position[1] + self.size):
                print(x ,y)
                for x1 in range(zoom):
                    for y1 in range(zoom):
                        print(x1 + x - position[0], y1 + y - position[1])
                        heights_n[x1 + (x - position[0]) * zoom + 1][y1 + (y - position[1]) * zoom + 1] = self.heights[x][y]
        print(len(self.heights))
        print(len(heights_n))
        return heights_n