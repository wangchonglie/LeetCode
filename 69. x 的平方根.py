"""
x 的平方根
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = (x >> 1) + 1
        while left < right:
            # 这里一定要取右中位数, 如果取左中位数, 代码可能会进入死循环
            mid = (left + right + 1) >> 1
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
        # 因为一定存在, 所以无需后处理
        return left
