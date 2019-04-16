import sys
import numpy as np
import copy

def main(m, n):
    # initial reached 
    maze = np.zeros((m, n))

    def dfs(x, y, reached):
      # depth first search
        if x == n or y == m or x < 0 or y < 0:
            # out of range
            return 0
        
        else:
            if reached[y][x] > 0:
                return 0
          
            reached_copy = copy.deepcopy(reached)
            reached_copy[y][x] += 1

            if reached_copy.all():
                return 1
            else:
                return dfs(x+1, y, reached_copy) + dfs(x-1, y, reached_copy) + dfs(x, y-1, reached_copy) + dfs(x, y+1, reached_copy)

    ans = dfs(0, 0, maze)
    print(int(ans))
