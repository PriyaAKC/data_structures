## FIFO DS : First In First Out
## Enqueue: data pushed into the Q from back end,Dequeue: popped out from other front end

# write the basic, display, push & pop operations
# Note, push => append at back & pop=> remove from 0 position : main difference from stack

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if not self.items:
            print("Empty List")
            return self.items == []

    def display_queue(self):
        #return self.items  #=> Should this be the case or below: use print(func_call) in that call
        for i in self.items:
            print(i)

    def enque(self, data): # same as push in stack
        self.items.append(data)

    def deque(self): ## similar  to pop in stack
        if not self.is_empty():
            self.items.pop(0)

    # def size(self):
    #     len(self.items)

    def __len__(self):
        return (len(self.items))


def main():
    que = Queue()
    que.is_empty()
    que.enque(8)
    # que.enque(9)
    # que.enque(10)
    que.display_queue() # call ussing print(fn) when return is used in fn definition
    print("####")
    que.deque()
    que.display_queue()
    print("####")
    print("Size",que.__len__())
    print(len(que))# so how to differentiate!! QS


if __name__ == "__main__":
    main()
