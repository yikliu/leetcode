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
from collections import deque

def shortestPath(grid: List[List[int]], k: int) -> int:
    m = len(grid)
    n = len(grid[0])
    q = deque()
    maxint = sys.maxint
    visited = [[maxint] * n] * m
    if gridp[0][0] == 0:
        q.append(0, 0, 0) # [x, y, currently_count_of_eliminated_obs]
        visited[0][0] = 0
    else:
        if k < 1:
            return -1
        else:
            q.append(0, 0, 1)
            visited[0][0] = 1

    steps = 0
    while q:
        cur_size = len(q)
        while cur_size > 0:
           cur_set = q.popleft()
            if cur_set[0] == m - 1 and cur_set[1] == n - 1:
                return steps

            for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                cur_i = i + di
                cur_j = j + dj
                if cur_i < 0 or cur_i >= m or cur_j < 0 or cur_j >= n:
                    continue
                elim_count = grid[cur_i][cur_j] + cur_set[2]
                if elim_count > k or visited[cur_i][cur_j] < k:
                    continue

                q.append([cur_i, cur_j, elim_count])
                visited[cur_i, cur_j] = elim_count
            cur_size -= 1
        steps += 1
    return -1

