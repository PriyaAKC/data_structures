# FIFO DS : First In First Out
# Enqueue: data pushed into the Q from back end,Dequeue: popped out from other front end

# write the basic, display, push & pop operations
# Note, push => append at back & pop=> remove from 0 position : main difference from stack


class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def display_queue(self):
        # return self.items  #=> Should this be the case or below: use print(func_call) in that call
        for i in self.items:
            print(i, end=" ")
        print("")

    def enqueue(self, data):  # same as push in stack
        self.items.append(data)

    def dequeue(self):  # similar  to pop in stack
        if not self.is_empty():
            return self.items.pop(0)

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
    que.dequeue()
    que.display_queue()
    print("####")
    print("Size", que.size())
    print(len(que))  # so how to differentiate!! QS


if __name__ == "__main__":
    main()
