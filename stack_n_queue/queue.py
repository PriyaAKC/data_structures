# FIFO DS : First In First Out
# Enqueue: data pushed into the Q from back end,Dequeue: popped out from other front end

# write the basic, display, push & pop operations
# Note, push => append at back & pop=> remove from 0 position : main difference from stack


class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        if not self.items:
            print("Empty List")
        return len(self.items) == 0

    def display_queue(self):
        for i in self.items:
            print(i, end=" ")
        print("")

    def enqueue(self, data):  # same as push in stack
        self.items.append(data)

    def dequeue(self):  # similar  to pop in stack
        if not self.is_empty():
            return self.items.pop(0)

    def peep(self):
        if not self.is_empty():
            return self.items[0]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()


def main():
    que = Queue()
    print(que.is_empty())
    que.enqueue(8)
    que.enqueue(9)
    que.enqueue(10)
    que.display_queue()  # call using print(fn) when return is used in fn definition
    print("####")
    print(que.peep())
    print("****")
    que.dequeue()
    que.display_queue()
    print("####")
    print("Size", que.size())
    print(len(que))


if __name__ == "__main__":
    main()
