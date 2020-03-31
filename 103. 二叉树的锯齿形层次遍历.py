"""
二叉树的锯齿形层次遍历
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
"""
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :param root: TreeNode
        :return: List[List[int]]
        """
        ret = []
        level_list = deque()
        if root is None:
            return []
        # 在第0层添加分隔符
        node_queue = deque([root, None])
        is_order_left = True

        while len(node_queue) > 0:
            cur_node = node_queue.popleft()
            if cur_node:
                if is_order_left:
                    level_list.append(cur_node.val)
                else:
                    level_list.appendleft(cur_node.val)

                if cur_node.left:
                    node_queue.append(cur_node.left)
                if cur_node.right:
                    node_queue.append(cur_node.right)
            else:
                # 完成了一层的遍历
                ret.append(list(level_list))
                # 换层的时候添加分隔符
                if len(node_queue) > 0:
                    node_queue.append(None)
                # 准备下一层的遍历
                level_list = deque()
                is_order_left = not is_order_left
        return ret
