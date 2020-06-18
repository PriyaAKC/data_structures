from stack_n_queue import queue
from binary_tree_search_traversal import binary_node


class BinaryTree(object):
    def __init__(self, root):
        self.root = binary_node.Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            self.__dfs_pre_order_display(self.root)
        elif traversal_type == "inorder":
            self.__dfs_in_order_display(self.root)
        elif traversal_type == "postorder":
            self.__dfs_post_order_display(self.root)
        elif traversal_type == 'levelorder':
            self.__level_order_traversal(self.root)
        else:
            print("Traversal type {} is not supported.".format(traversal_type))
        print("")

    def __dfs_pre_order_display(self, start):
        """
        Order : "Root->Left->Right"
        :param start: node that gets updated on every recursive call of the function
        :return:
        """
        if start:
            print(start, end=" ")
            self.__dfs_pre_order_display(start.left)
            self.__dfs_pre_order_display(start.right)

    def __dfs_in_order_display(self, start):
        """
        Order : "Left->Root->Right"
        """
        if start:
            self.__dfs_in_order_display(start.left)
            print(start, end=" ")
            self.__dfs_in_order_display(start.right)

    def __dfs_post_order_display(self, start):
        """
        Order : "Left->Right->Root"
        """
        if start:
            self.__dfs_post_order_display(start.left)
            self.__dfs_post_order_display(start.right)
            print(start, end=" ")

    @staticmethod
    def __level_order_traversal(start):
        """
        the idea in this case is unlike the methods(orders) of DFS traversal which are recursive, same can't be applied
        Hence to traverse at tree at each level, use of another data structure with appropriate logic is used
        :param start:
        :return:
        """
        if start is None:
            print("Empty Tree!")
            return

        que = queue.Queue()
        que.enqueue(start)

        # Now a while loop can be run to iterate through the elements
        while que.size() > 0:  # should be printed & check its children till its empty
            node = que.dequeue()  # this returns node, not value
            print(node, end=" ")  # can alternatively define peek function in the class defn of queue

            if node.left:
                que.enqueue(node.left)
            if node.right:
                que.enqueue(node.right)


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
    two = binary_node.Node(2)
    three = binary_node.Node(3)
    four = binary_node.Node(4)
    five = binary_node.Node(5)
    six = binary_node.Node(6)
    seven = binary_node.Node(7)
    eight = binary_node.Node(8)
    nine = binary_node.Node(9)

    tree.root.left = two
    tree.root.right = three
    two.left = four
    two.right = five
    five.left = six
    five.right = seven
    three.left = eight
    three.right = nine

    print("PreOrder Traversal")
    tree.print_tree('preorder')  # "Ro->L->Ri"  # 1-2-4-5-6-7-3-8-9-
    print("InOrder Traversal")
    tree.print_tree('inorder')  # "L->Ro->Ri" # 4-2-6-5-7-1-8-3-9-
    print("PostOrder Traversal")
    tree.print_tree('postorder')  # "L->Ri->Ro" # 4-6-7-5-2-8-9-3-1-
    print("LevelOrder Traversal")
    tree.print_tree('levelorder')


if __name__ == '__main__':
    main()

# Tree traversal Algorithms: process visiting/updating a node exactly once in the traversal
# In Tree Structure, have different traversal algorithms as compared to LinkedList which are mostly linear
# Cases :Depth First Search & Breath First Search Order
# -> Three flavors of DFS : pre-order, in-order and post-order traversals
