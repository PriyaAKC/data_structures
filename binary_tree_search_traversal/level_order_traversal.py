from binary_tree_search_traversal import binary_tree
from stack_n_queue import queue


def level_order_traversal(start):
    """
    the idea in this case is unlike the methods(orders) of DFS traversal which are recursive, same can't be applied
    Hence to traverse at tree at each level, use of another data structure with appropriate logic is used
    :param bin_tree:
    :return:
    """
    if start is None:
        return

    ## assert strat input is an instance of binary tree : can that be done?

    que = queue.Queue()
    que.enque(start)
    print("Start", start.left)

    # Now a while loop can be run to iterate through the elements
    traversal = ""
    while que.__len__() > 0:  # should be printed & check its children till its empty
        print("in")
        traversal += (str(start.data) + "-")  # can alternatively define peek function in the class defn of queue
        node = que.deque()  # this returns node, not value

        if node.left:
            que.enque(node.left)
        if node.right:
            que.enque(node.right)

    return traversal


tree = binary_tree.BinaryTree(1)
Node = binary_tree.Node
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.left = Node(6)
tree.root.left.right.right = Node(7)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

print(level_order_traversal(tree.root))
