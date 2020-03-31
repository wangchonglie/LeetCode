"""
缺失的第一个正数(与442题类似)
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

 

示例 1:
输入: [1,2,0]
输出: 3

示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1

提示：
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

                # 这种方式不行, 因为先交换了 nums[i] 的值, 导致 nums[i] - 1 的值不是预期的值
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
        for i in range(n):
            if nums[i] - 1 != i:
                return i + 1
        return n + 1


s = Solution()
print(s.firstMissingPositive([3, 4, -1, 1]))
print(1 ^ 2 ^ 2)
