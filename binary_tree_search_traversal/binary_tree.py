from stack_n_queue import queue


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.dfs_pre_order_display(self.root)
        elif traversal_type == "inorder":
            return self.dfs_in_order_display(self.root)
        elif traversal_type == "postorder":
            return self.dfs_post_order_display(self.root)
        elif traversal_type == 'levelorder':
            return self.level_order_traversal(self.root)
        else:
            print("Traversal type {} is not supported.".format(traversal_type))

    def dfs_pre_order_display(self, start):
        """
        Order : "Root->Left->Right"
        :param start: node that gets updated on every recursive call of the function
        :param traversal: string displaying the result on every recursive call
        :return:
        """
        if start:
            print(start.data, end=" ")
            self.dfs_pre_order_display(start.left)
            self.dfs_pre_order_display(start.right)

    def dfs_in_order_display(self, start):
        """
        Order : "Left->Root->Right"
        """
        if start:
            self.dfs_in_order_display(start.left)
            print(start.data, end=" ")
            self.dfs_in_order_display(start.right)

    def dfs_post_order_display(self, start):
        """
        Order : "Left->Right->Root"
        """
        if start:
            self.dfs_post_order_display(start.left)
            self.dfs_post_order_display(start.right)
            print(start.data, end=" ")

    def level_order_traversal(self, start):
        """
        the idea in this case is unlike the methods(orders) of DFS traversal which are recursive, same can't be applied
        Hence to traverse at tree at each level, use of another data structure with appropriate logic is used
        :param start:
        :return:
        """
        if start is None:
            return

        que = queue.Queue()
        que.enque(start)

        # Now a while loop can be run to iterate through the elements
        while que.size() > 0:  # should be printed & check its children till its empty
            node = que.deque()  # this returns node, not valu
            print(node.data, end=" ")  # can alternatively define peek function in the class defn of queue

            if node.left:
                que.enque(node.left)
            if node.right:
                que.enque(node.right)

        print("")


#  Tree construct:
#      1
#    /   \
#   2     3
#  /\     /\
# 4  5   8  9
#    /\
#   6  7
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
    print("PreOrder Traversal")
    tree.print_tree('preorder')  # "Ro->L->Ri"  # 1-2-4-5-6-7-3-8-9-
    print("\nInOrder Traversal")
    tree.print_tree('inorder')  # "L->Ro->Ri" # 4-2-6-5-7-1-8-3-9-
    print("\nPostOrder Traversal")
    tree.print_tree('postorder')  # "L->Ri->Ro" # 4-6-7-5-2-8-9-3-1-
    print("\nLevelOrder Traversal")
    tree.print_tree('levelorder')


if __name__ == '__main__':
    main()

# Tree traversal Algorithms: process visiting/updating a node exactly once in the traversal
# In Tree Structure, have different traversal algorithms as compared to LinkedList which are mostly linear
# Cases :Depth First Search & Breath First Search Order
# -> Three flavors of DFS : pre-order, in-order and post-order traversals
