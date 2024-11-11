class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def printLeafNodes(self, node):
        if node is None:
            return

        if node.left is None and node.right is None:
            print(node.data, end=' ')
            return

        self.printLeafNodes(node.left)
        self.printLeafNodes(node.right)

    def countEdges(self, node):
        if node is None:
            return 0

        left_edges = self.countEdges(node.left)
        right_edges = self.countEdges(node.right)

        return left_edges + right_edges + (1 if node.left or node.right else 0)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print("Leaf nodes:")
    tree.printLeafNodes(tree.root)

    print("\nTotal edges:")
    print(tree.countEdges(tree.root))
