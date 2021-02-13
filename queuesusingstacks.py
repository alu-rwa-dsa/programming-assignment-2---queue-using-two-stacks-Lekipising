

# Node class
class Node():
    def __init__(self):
        self.val = -1
        self.next = None


# stack class
class stack():
    def __init__(self):
        super().__init__()
        self.head = None
        self.no_of_items = 0

    def isEmpty(self):
        return self.head == None

    def push(self, val):
        headold = self.head
        self.head = Node()
        self.head.val = val
        self.head.next = headold

    def pop(self):
        if self.head == None:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.val


class queue():
    def __init__(self):
        super().__init__()
        self.s1 = stack()
        self.s2 = stack()

    # enqueue item x
    def push(self, x):
        self.s1.push(x)
    
    # dequeue
    def pop(self):
        # check if first stack is empty
        if self.s1.isEmpty():
            # pop from second stack
            return self.s2.pop()
        else:
            # check if second stack is not empty
            if not self.s2.isEmpty():
                # pop from second stack
                return self.s2.pop()
            else:
                # push items to second stack
                while True:
                    # pop from first stack
                    a = self.s1.pop()
                    if self.s1.isEmpty():
                        break
                    # push to second
                    self.s2.push(a)
                return a

    # return front
    def peek(self):
        if not self.s2.isEmpty():
            return self.s2.peek()
        while not self.s1.isEmpty():
            # pop from first stack, push to second
            self.s2.push(self.s1.pop())
        return self.s2.peek()


# number of queries/operations to perform
n_queries = int(input().strip())

# create a queue
q1 = queue()

# perform queries
for i in range(n_queries):
    query = input().strip().split()
    # enqueue
    if query[0] == '1':
        q1.push(int(query[1]))
        # dequeue
    elif query[0] == '2':
        q1.pop()
    # print front
    elif query[0] == '3':
        print(q1.peek())
