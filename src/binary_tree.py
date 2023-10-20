class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)


def sum_of_depths(root, depth=0, sum_depth=None):
    if sum_depth is None:
        sum_depth = []
    if root is not None:
        sum_depth.append(depth)
        if root.left:
            sum_of_depths(root.left, depth + 1, sum_depth)
        if root.right:
            sum_of_depths(root.right, depth + 1, sum_depth)
    return sum(sum_depth)



print(sum_of_depths(root))
