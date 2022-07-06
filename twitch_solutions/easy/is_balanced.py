# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isLeaf(self, node):
        return node.left is None and node.right is None

    def length(self, node, ln):
        if self.isLeaf(node):
            return ln
        len_left = ln
        if node.left:
            len_left = self.length(node.left, ln + 1)
        len_right = ln
        if node.right:
            len_right = self.length(node.right, ln + 1)
        return 



    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return abs(self.length(root.left, 0) - self.length(root.right, 0)) < 2