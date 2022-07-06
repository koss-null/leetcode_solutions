# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = list()
        if root.left:
            res = self.inorderTraversal(root.left)
        res.append(root.val)
        if root.right:
            for t in self.inorderTraversal(root.right):
                res.append(t)
        return res
        

        