from binary_tree_search_traversal.binary_tree import BinaryTree
from binary_tree_search_traversal.binary_node import Node
from stack_n_queue import queue


def level_order_traversal(start):
    """
    the idea in this case is unlike the methods(orders) of DFS traversal which are recursive, same can't be applied
    Hence to traverse at tree at each level, use of another data structure with appropriate logic is used
    :param start:BinaryTree
    :return:
    """
    if start is None:
        return

    if not isinstance(start, Node):
        return

    que = queue.Queue()
    que.enqueue(start)

    # Now a while loop can be run to iterate through the elements
    traversal = ""
    while que.size() > 0:  # should be printed & check its children till its empty
        node = que.dequeue()  # this returns node, not value
        traversal += (str(node.data) + "-")  # can alternatively define peek function in the class defn of queue

        if node.left:
            que.enqueue(node.left)
        if node.right:
            que.enqueue(node.right)

    return traversal


def main():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.left.right.left = Node(6)
    tree.root.left.right.right = Node(7)
    tree.root.right.left = Node(8)
    tree.root.right.right = Node(9)

    tree.print_tree("inorder")

    print(level_order_traversal(tree.root))


if __name__ == '__main__':
    main()
