from linked_list import node

class Circular_LinkedList():
    """
    The circle in assumed to be from last element to first
    No need to inherit Node class as it remains the same
    """

    def __init__(self):
        self.head = None
        self.size = 0

    def display_list(self):
        curr_node = self.head

        if self.head is None:
            print("Empty List!")
            return
        while curr_node.next != self.head:
            print(curr_node.data)
            curr_node = curr_node.next
        print(curr_node.data)

    def add_at_begin(self, data):
        new_node = node.Node(data)
        curr_node = self.head

        if self.head is None:
            print("Empty list, adding first element")
            new_node.next = new_node
            self.head = new_node
            return

        new_node.next = curr_node
        while curr_node.next != self.head:
            curr_node = curr_node.next

        curr_node.next = new_node
        self.head = new_node
        self.size += 1

    def add_at_end(self, data):
        new_node = node.Node(data)
        p = self.head
        if self.head is None:
            print("Empty Loop, Adding 1st element")
            self.head = new_node
            self.head.next = self.head
            self.size += 1
            # print("Node added at end")
            return
        while p.next != self.head:
            p = p.next
        # print("Reached the end")
        p.next = new_node
        new_node.next = self.head
        self.size += 1

    def remove_node(self, data):
        """
       Assumption unique value exist and that only the 1st occurrence is removed!
        """
        curr = self.head
        p = self.head

        if self.head is None:
            print("Empty List, nothing to remove")
            return

        # Special case of data at head
        if curr.val == data:
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
            self.size -= 1
            print("Removed 1st node")
            return

        # going till last in search, coz p.next will always exist but cant check with p
        while p.next != self.head:
            if p.next.val == data:
                p.next = p.next.next
                self.size -= 1
                print("Node found and removed")
                return
            p = p.next

        # checking for last node
        if p.next.val == data:
            p.next = self.head
            self.size -= 1
            print("Node was last, removed")
        print("Node not found!")

    def split_at_k(self, position):
        """
        Split the CLL into 2 separate CLL!
        """
        curr_node = self.head
        position_track = 1
        prev = None

        if self.size == 1:
            print("Only 1 node, cannot be split")
            return

        # for remaining all positions & cases
        while position_track <= self.size:
            # print("position_track", position_track)
            prev = curr_node
            curr_node = curr_node.next

            if position_track == position:
                print("position matched!")
                prev.next = self.head
                self.size = position_track

                # new CCL
                cc_new = Circular_LinkedList()
                while curr_node.next != self.head:
                    cc_new.add_at_end(curr_node.data)
                    curr_node = curr_node.next
                cc_new.add_at_end(curr_node.data)

                print("Old List")
                self.display_list()
                print("\n")
                print("New List")
                cc_new.display_list()
                return

            position_track += 1
        print("Position not found!")


def main():
    clist = Circular_LinkedList()
    clist.display_list()
    clist.add_at_begin(7)
    clist.add_at_begin(8)
    print("size", clist.size)
    clist.display_list()
    print("#############")
    clist.add_at_end(9)
    clist.add_at_end(10)
    print("size", clist.size)
    clist.display_list()
    print("#############")
    clist.split_at_k(2)
    print("#############")
    print("size", clist.size)
    clist.display_list()


if __name__ == "__main__":
    main()
