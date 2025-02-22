from constant import *

class Grid_visual(object):
    def __init__(self, position, heights):
        self.position = position
        self.heights = heights
        self.size = len(heights) // zoom

    def transform(self, position_n):
        heights_n = [[0 for i in range(len(self.heights))] for j in range(len(self.heights))]
        position = ((len(self.heights) - (self.size // 2 - 1) * 2) // 2) + position_n[0], \
                   ((len(self.heights) - (self.size // 2 - 1) * 2) // 2) + position_n[1]

        for x in range(position[0], position[0] + self.size):
            for y in range(position[1], position[1] + self.size):

                for x1 in range(zoom):
                    for y1 in range(zoom):

                        heights_n[x1 + (x - position[0]) * zoom + 1][y1 + (y - position[1]) * zoom + 1] = self.heights[x][y]

        return heights_n

    def changes_heights(self, position_c):
        self.heights[position_c[0]][position_c[1]] = 0
