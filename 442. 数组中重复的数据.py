"""
数组中重复的数据(与41题类似)

给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
找到所有出现两次的元素。
你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
示例：
输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]
"""
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        res = []
        for i in range(n):
            if i != nums[i] - 1:
                res.append(nums[i])
        return res
