class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.start = None
        self.last = None
        self.length = 0

    def isnone(self):
        if self.start is None:
            return True

    def add_first(self, value):
        node = LinkedList.Node(value)
        if self.isnone():
            self.start = node
        else:
            node.next = self.start
            self.start = node

        self.length += 1

    def add_last(self, value):
        node = LinkedList.Node(value)
        if self.isnone():
            self.start = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

        self.length += 1

    def index_of(self, value):
        node = LinkedList.Node(value)
        temp = self.start
        index = 0
        while temp != self.last:
            if temp.value == node.value:
                return index
            temp = temp.next
            index += 1
        return -1

    def contains(self, value):
        if self.index_of(value) != -1:
            return True
        else:
            return False

    def remove_first(self):
        if self.isnone():
            raise ValueError('LinkedList is Empty')
        elif self.start == self.last:
            self.start = self.last = None
        else:
            self.start = self.start.next

        self.length -= 1

    def remove_last(self):
        if self.isnone():
            raise ValueError('LinkedList is Empty')
        elif self.start == self.last:
            self.start = self.last = None
        else:
            temp = self.start
            while temp.next != self.last:
                temp = temp.next
            temp.next = None
            self.last = temp

        self.length -= 1

    def size(self):
        return self.length

    def __str__(self):
        if self.isnone():
            raise ValueError('LinkedList is Empty')
        temp = self.start
        while temp is not None:
            print(temp.value)
            temp = temp.next
        return 'done'


l = LinkedList()
l.add_last(10)
l.add_last(20)
l.add_last(30)
l.add_last(40)
l.add_first(50)
l.remove_first()
l.remove_last()
print(l.size())
print(l)
