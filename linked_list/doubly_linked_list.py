class Node(object):
    """
    Node class for doubly linked list
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLL:

    def __init__(self):
        self.head = None  # note no need to define the next/prv attribute: Why? coz you never did :P
        self.size = 0

    def display(self):
        curr_node = self.head

        if curr_node is None:
            print("Empty List")
            return
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

    def add_at_begin(self, data):
        curr_node = self.head

        # Create nee Dll node
        new_node = Node(data)

        # Check for empty list
        if curr_node is None:
            print("Empty List, adding 1st element")
            self.head = new_node
            self.size += 1
            return

        # next of new nod
        # new_node.next = self.head.next !!!Need to think in terms of two way connections
        self.head.prev = new_node  # from None update to ne node
        new_node.next = self.head
        self.head = new_node
        new_node.prev = None  # Is this redundant ; by defn its already right?
        self.size += 1

    #         while curr_node.next is not None: No need yo traverse till end its a dll, not circular
    #             curr_node = curr_node.next
    #         curr_node.next = new_node
    #         self.head = curr_node
    #         self.size +=1

    def add_at_end(self, data):
        curr_node = self.head

        # Create nee Dll node
        new_node = Node(data)

        # Check for empty list
        if curr_node is None:
            print("Empty List, adding 1st element")
            self.head = new_node
            self.size += 1
            return

        while curr_node.next is not None:
            curr_node = curr_node.next
        new_node.next = curr_node.next  # thats basiclly none
        curr_node.next = new_node  # is this redundant?? No!
        new_node.prev = curr_node  # This becomes important to define in double, prev kya hai??
        self.size += 1

    def add_before_node(self, data, position):
        curr_node = self.head
        new_node = Node(data)
        counter = 0

        # spl case of position =1
        if position == 1:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = None  # required?

        while counter != position - 1:
            curr_node = curr_node.next
            counter += 1
        new_node.next = curr_node.next
        new_node.prev = curr_node
        curr_node.next.prev = new_node
        curr_node.next = new_node
        self.size += 1


def main():
    dll = DoubleLL()
    dll.add_at_begin(4)
    dll.add_at_end(5)
    print("Size", dll.size)
    dll.display()


if __name__ == '__main__':
    main()
