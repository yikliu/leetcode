'''
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

 Example 1:
 Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
 Output: 6
 Explanation: 
 The shortest path without eliminating any obstacle is 10.
 The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

 Example 2:
 Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
 Output: -1
 Explanation: We need to eliminate at least two obstacles to find such a walk.
  

  Constraints:

  m == grid.length
  n == grid[i].length
  1 <= m, n <= 40
  1 <= k <= m * n
  grid[i][j] is either 0 or 1.
  grid[0][0] == grid[m - 1][n - 1] == 0
'''

import unittest
from typing import List
import heapq

def shortestPath(grid: List[List[int]], k: int) -> int:
    m = len(grid)
    n = len(grid[0])
   
    # visited[2] if one of the dimensions needed to store the state. 
    visited = set([0, 0, k]) 

    q=[(0, 0, 0, k)]

    while q:
      l, r, c, kr = heapq.heappop(q) 
      
      if r == m - 1 and c == n - 1:
        return l

      for nxt in ([r - 1, c], [r + 1, c], [r, c + 1], [r, c -1]):
        if nxt[0] >= 0 and nxt[1] >= 0 and nxt[0] < m and nxt[1] < n: 
            if grid[nxt[0]][nxt[1]] == 1:
                if kr > 0 and (nxt[0], nxt[1], kr - 1) not in visited:
                    heapq.heappush(q, (l + 1, nxt[0], nxt[1], kr - 1))
                    visited.add((nxt[0], nxt[1], kr - 1))
            elif (nxt[0], nxt[1], kr) not in visited:
                heapq.heappush(q, (l + 1, nxt[0], nxt[1], kr))
                visited.add((nxt[0], nxt[1], kr))
    return -1 
            

class testShortestPathObstacleElimination(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(6, shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1))

    def testImpossible(self):
        self.assertEqual(-1, shortestPath([[0,1,1],[1,1,1],[1,0,0]], 1))

if __name__ == '__main__':
    unittest.main()

