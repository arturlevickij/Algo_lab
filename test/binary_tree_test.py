from unittest import TestCase, main
from binary_tree import TreeNode, sum_of_depths

class Test_binary_tree(TestCase):
    def test_case1(self):
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.left.left = TreeNode(4)
        root1.left.right = TreeNode(5)
        root1.right = TreeNode(3)
        res = sum_of_depths(root1)
        self.assertEqual(res, 6)

    def test_case2(self):
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        res = sum_of_depths(root2)
        self.assertEqual(res, 1)

    def test_case3(self):
        root3 = None
        res = sum_of_depths(root3)
        self.assertEqual(res, 0)

    def test_case4(self):
        root4 = TreeNode(1)
        root4.left = TreeNode(2)
        root4.left.left = TreeNode(4)
        root4.left.right = TreeNode(5)
        root4.right = TreeNode(3)
        root4.right.right = TreeNode(6)
        res = sum_of_depths(root4)
        self.assertEqual(res, 8)
