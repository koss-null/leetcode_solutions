# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check(p, q)
        