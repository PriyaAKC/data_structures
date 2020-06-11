from linked_list import node


class Singly_LinkedList():

    def __init__(self):
        self.head = None  # initialize the head pointer: Each SLL instance will maintain single ref to 1st node

    def create_list(self):
        n = int(input("Enter the number of nodes"))
        if n == 0:
            return
        for i in range(n):
            print("Enter element at position", i + 1)
            data = int(input("Enter element "))
            self.insert_end(data)
            print("Entering new node")

    def display_list(self):
        p = self.head
        if p is None:
            print('List is empty')
            return
        while p is not None:
            print(p.data)
            p = p.next

    def count(self):
        p = self.head
        count = 0
        if p is None:
            print("Empty List")
            return
        while p is not None:
            count += 1
            p = p.next
            return count

    def search(self, item):  # if elem exists , return position
        p = self.head
        position = 1
        if p is None:
            print("Empty List")
            return
        while p is not None:
            if p.data == item:
                print("Condition matched")
                print(item, "is at position", position)
                return True
            p = p.next
            position += 1

        print("Element not found")
        return False

    ### Insert methods ###

    def insert_begin(self, data):
        new = node.Node(data)
        new.next = self.head
        self.head = new
        print("Inserted at beginning")

    def insert_end(self, data):
        new = node.Node(data)

        # for empty case
        if self.head is None:
            print("Empty List, adding first element")
            self.head = new
            return

        p = self.head
        while p.next is not None:
            p = p.next
        p.next = new
        print("Inserted at end")

    def data_at_position(self, k):
        p = self.head
        position = 0
        while p.next != None:
            print("inside while loop")
            if position == k - 1:
                print("in condition")
                return p.data
            p = p.next
            position += 1

        print("Position not found")
        return

    def insert_at_position(self, data, k):
        new = node.Node(data)
        p = self.head
        idx = 0
        while p.next is not None:
            if idx == k - 1:
                new.next = p.next
                p.next = new
                print("Inserted at position", k)
                return
            p = p.next
            idx += 1
            print("Position not found")

    def insert_after(self, item,val):
        p = self.head
        position = 1

        if p is None:
            print("Empty List")

        while p is not None:
            if p.data == item:
                self.insert_at_position(val, position)
            p = p.next
            position += 1

    def insert_before(self, item, val):
        p = self.head
        position = 1

        if p is None:
            print("Empty List")

        while p is not None:
            if p.data == item:
                self.insert_at_position(val, position - 1)
            p = p.next
            position += 1

    def del_node(self, item):
        p = self.head

        if p is None:
            print("Empty List")

        while p is not None:
            if p.next.data == item:
                p.next = p.next.next
                return
            p = p.next
            print("Node not found")

    def del_first_node(self):
        self.head = self.head.next

    def del_last_node(self):
        p = self.head
        while p.next.next is not None:
            p = p.next

        p.next = None


def main():
    new_list = Singly_LinkedList()
    new_list.insert_begin(4)
    new_list.insert_end(5)
    new_list.insert_at_position(10, 1)
    new_list.insert_after(10, 25)
    new_list.insert_before(3, 39)
    print(new_list.display_list()) # Why does none get printed?
    print("####")
    # new_list.search(3)
    # new_list.del_last_node()
    # new_list.display_list()
    # print("####")


if __name__ == '__main__':
    main()
