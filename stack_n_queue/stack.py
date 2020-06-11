# Stack : FILO First In-> Last Out : modification of a list

# Operations : Push & Pop ; Fundamental


class Stack():

    def __init__(self):
        self.items = []  # begin with an empty list, easily use lists built-in functions

    def is_empty(self):
        if not self.items:
            print("Empty Stack!")
        return self.items == []

    def display_stack(self):
        return self.items

    def push(self, data):
        self.items.append(data)

    def pop(self):  # removes the last item
        if not self.is_empty():
            return self.items.pop()

    def peek(self):  # look at last item in the stack
        if not self.is_empty():
            return self.items[-1]


def main():
    s = Stack()
    s.is_empty()
    s.push(1)
    s.push(3)
    s.push(5)
    s.is_empty()
    print(s.display_stack())
    s.pop()
    print(s.display_stack())


if __name__ == '__main__':
    main()
