"""
你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，
你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。

我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
如果我们的地图上只有陆地或者海洋，请返回 -1。

示例 1：
输入：[[1,0,1],[0,0,0],[1,0,1]]

输出：2
解释：
海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。

示例 2：
输入：[[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释：
海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。

提示：
1 <= grid.length == grid[0].length <= 100
grid[i][j] 不是 0 就是 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/as-far-from-land-as-possible
"""
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 将陆地坐标位置加入队列
        # q = []
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j]:
        #             q.append([i, j])
        q = [[i, j] for i in range(n) for j in range(n) if grid[i][j]]
        if len(q) == 0 or len(q) == n * n:
            return -1

        # 方向列表
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        while q:
            # loc 用来存陆地的坐标位置
            loc = q.pop(0)
            x, y = loc[0], loc[1]
            # 在当前点向上下左右方向前进
            for i in range(4):
                new_x = dx[i] + x
                new_y = dy[i] + y
                # 目标点是否越界或者已访问过
                if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n or grid[new_x][new_y]:
                    continue
                # 弱朝当前陆地的某个方向前进, 且目的地是海洋的, 把它占领成陆地, 将目的地位置上的数字加1, 代表前进1, 也就是距离加1
                grid[new_x][new_y] = grid[x][y] + 1
                # 将新占领的陆地坐标位置加入队列
                q.append([new_x, new_y])
        # 因为初始位置的陆地值为1, 多加了1, 所以最后要减1
        return grid[loc[0]][loc[1]] - 1


s = Solution()
grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
print(s.maxDistance(grid))
