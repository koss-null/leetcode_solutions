# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def check(self, head1: Optional[TreeNode], head2: Optional[TreeNode],) -> bool:
        if head1 is None and head2 is None:
            return True
        if head1 is None or head2 is None:
            return False

        if head1.val != head2.val:
            return False
        if not self.check(head1.left, head2.left):
            return False
        if not self.check(head1.right, head2.right):
            return False

        return True
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root.left, root.right)
        