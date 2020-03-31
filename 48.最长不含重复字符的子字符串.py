"""
最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 
提示：
s.length <= 40000
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        1. 遍历字符串，过程中将出现过的字符存入字典，key为字符，value为字符下标
        2. 用maxLength保存遍历过程中找到的最大不重复子串的长度
        3. 用start保存最长子串的开始下标
        4. 如果字符已经出现在字典中，更新start的值
        5. 如果字符不在字典中，更新maxLength的值
        """
        start = max_length = 0
        used_char = dict()
        for idx in range(len(s)):
            if s[idx] in used_char and start <= used_char[s[idx]]:
                start = used_char[s[idx]] + 1
            else:
                max_length = max(max_length, idx - start + 1)
            used_char[s[idx]] = idx
        return max_length
