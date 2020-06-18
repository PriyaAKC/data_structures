from linked_list import node


class DNode(node.Node):
    """
    DNode class for doubly linked list inheriting Node class from node
    Adding new attributes
    """

    def __init__(self, data):
        super(DNode, self).__init__(data)
        self.prev = None


class Doubly_LinkedList(object):
    """
    Operations performed
    """

    def __init__(self):
        self.head = None
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

        # Create new DLL node
        new_node = DNode(data)

        # Check for empty list
        if curr_node is None:
            print("Empty List, adding 1st element")
            self.head = new_node
            self.size += 1
            return
        # from None update to new node
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        new_node.prev = None
        self.size += 1

    def add_at_end(self, data):
        curr_node = self.head

        # Create nee DLL node
        new_node = DNode(data)

        # Check for empty list
        if curr_node is None:
            print("Empty List, adding 1st element")
            self.head = new_node
            self.size += 1
            return

        while curr_node.next is not None:
            curr_node = curr_node.next
        new_node.next = curr_node.next
        curr_node.next = new_node
        new_node.prev = curr_node
        self.size += 1

    def add_before_position(self, data, position):
        curr_node = self.head
        new_node = DNode(data)
        counter = 1

        # spl case of position =1
        if position == 1:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = None

        while counter != position - 1:
            print("in")
            curr_node = curr_node.next
            counter += 1
        curr_node.next.prev = new_node
        new_node.next = curr_node.next
        new_node.prev = curr_node
        curr_node.next = new_node
        self.size += 1

    def add_after_position(self, data, position):
        new_node = DNode(data)
        curr_node = self.head
        counter = 0

        if position == 1:
            self.add_at_begin(data)
            return
        if position == self.size:
            self.add_at_end(data)
            return

        while counter != position:
            curr_node = curr_node.next
            counter += 1
        curr_node.next.prev = new_node  #
        new_node.next = curr_node.next
        new_node.prev = curr_node
        curr_node.next = new_node
        self.size += 1

    def del_node(self, key):
        curr_node = self.head

        while curr_node:
            # Case1 : when key is at the head
            if curr_node.prev is None and curr_node.data == key:
                curr_node.next.prev = None
                self.head = curr_node.next
                curr_node = None
                return
            # Case2
            elif curr_node.next is None and curr_node.data == key:
                prev = curr_node.prev
                prev.next = None
                curr_node = None
                return
            # Case 3: when key in middle somewhere
            elif curr_node is not None and curr_node.data == key:
                prev = curr_node.prev
                prev.next = curr_node.next
                curr_node.next.prev = prev
                curr_node = None
                return
        curr_node = curr_node.next

    def reverse(self):  # Update for efficient method


        begin_point = self.head
        end_point = self.head

        while end_point.next:  # Not very efficient since, you need to go through entire loop once already
            end_point = end_point.next
        temp = -1
        count = 1

        while count <= int(self.size // 2):
            temp = begin_point.data
            begin_point.data = end_point.data
            end_point.data = temp
            begin_point = begin_point.next
            end_point = end_point.prev
            count += 1
        print(self.head.data)

    def remove_duplicates(self):  # Update for correctness
        unique_set = set()
        curr_node = self.head

        while curr_node:
            if curr_node.data in unique_set:
                print("Duplicate removed", curr_node.data)
                self.del_node(curr_node)
            else:
                unique_set.add(curr_node.data)

    def sum_pairs(self, value):
        curr_node = self.head
        pairs = list()

        while curr_node:
            next_node = curr_node.next
            # print("In loop1")
            while next_node:
                # print("In loop2")
                sum_val = curr_node.data + next_node.data
                # print("sum_val",sum_val)
                if sum_val == value:
                    # print("pair found",curr_node.data, next_node.data )
                    # pairs.append((curr_node.data, next_node.data))
                    pairs.append((curr_node.data, next_node.data))
                    # return curr_node.data, next_node.data # Dont these get printed?
                if next_node.next is None:
                    break
                next_node = next_node.next
            if curr_node.next is None:
                break
            curr_node = curr_node.next
        if not pairs:  # Condition to check empty list : a short-circuit operator, so it only evaluates the second argument if the first one is false
            print("None such pairs found")  # empty sequences evaluate to false according to the PEP 8 standard
        return pairs


def main():
    dll = Doubly_LinkedList()
    dll.add_at_begin(3)
    dll.add_at_end(5)
    dll.display()
    print("##########")
    print("Size", dll.size)
    dll.add_before_position(4, 2)
    dll.display()
    print("##########")
    dll.add_after_position(6, 3)
    print("Size", dll.size)
    dll.display()
    print("##########")
    dll.del_node(3)
    dll.display()
    print("##########")
    dll.del_node(6)
    dll.display()
    dll.reverse()
    dll.display()
    dll.add_before_position(4, 2)
    dll.display()
    print("********")
    dll.remove_duplicates()
    dll.display()
    print("##########")
    print(dll.sum_pairs(12))


if __name__ == '__main__':
    main()
