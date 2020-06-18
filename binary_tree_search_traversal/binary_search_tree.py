# Given elements in an array and create a  BST

from binary_tree_search_traversal import binary_node


class BinarySearchTree:
    def __init__(self):  # , root
        self.root = None

    def _insert_helper(self, data, curr_node):
        if curr_node:  # this wont come here, otherwise you dont know hwre exactly to insert!!
            if data == curr_node.data:
                print("Value already present! No duplicates allowed")

            if data < curr_node.data:
                if curr_node.left is not None:
                    self._insert_helper( data, curr_node.left)
                else:
                    curr_node.left = binary_node.Node(data)


            elif data > curr_node.data:
                if curr_node.right is not None:
                    self._insert_helper( data, curr_node.right)
                else:
                    curr_node.right = binary_node.Node(data)

    def insert_node(self, data):

        if self.root is None:
            print("Empty Tree! creating first root node")
            self.root = binary_node.Node(data)
            return
        # create a helper method!! coz in this kind of recursion, while loop will not help to distinguish
        self._insert_helper(data, self.root)

    def _find_helper(self, data, curr_node):
        if data == curr_node.data:
            print("Node Found!")
            return True

        if data < curr_node.data and curr_node.left is not None:
            self._find_helper( data, curr_node.left)
        elif data < curr_node.data and curr_node.right is not None:
            self._find_helper( data, curr_node.right)
        else:
            print("Value not found!")
            return False


    def find_node(self, data):
        if self.root is None:
            print("Empty Tree!")
            return

        return self._find_helper(data, self.root)


def main():
    bst = BinarySearchTree()
    bst.insert_node(4)
    bst.insert_node(2)
    bst.insert_node(8)
    bst.insert_node(5)
    bst.insert_node(10)
    bst.find_node(2)
    # bst.find_node(3)
    # bst.find_node(7)
    bst.find_node(10) ### Debug, 5,10 not working!!


if __name__ == "__main__":
    main()
