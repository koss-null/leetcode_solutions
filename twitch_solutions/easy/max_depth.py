# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.md = 0

    def goDeeper(self, head, depth):
        if not head:
            return
        if depth > self.md:
            self.md = depth

        self.goDeeper(head.left, depth + 1)
        self.goDeeper(head.right, depth + 1)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.goDeeper(root, 1)
        return self.md