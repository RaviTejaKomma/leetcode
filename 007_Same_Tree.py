__author__ = 'Ravi Teja Komma'

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        result = False
        return self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)