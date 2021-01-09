class CircularLinkedList :
    class Node :
        def __init__(self, element, next):
            self.element = element
            self.next = next
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0

    def add_first(self, e):
        newest = self.Node(e, None)
        if self.is_empty():
            newest.next = newest
            self.head = newest
            self.tail = newest
        else :
            self.tail.next = newest
            newest.next = self.head
        self.head = newest
        self.size += 1

    def add_last(self, e):
        newest = self.Node(e, None)
        if self.is_empty():
            newest.next = newest
            self.head = newest
            self.tail = newest
        else:
            newest.next = self.head
            self.tail.next = newest
        self.tail = newest
        self.size += 1

    def add_any(self, e, pos):
        newest = self.Node(e, None)
        thead = self.head
        i = 1
        while i< pos :
            thead = thead.next
            i += 1
        newest.next = thead.next
        thead.next = newest
        self.size += 1

    def del_first(self):
        if self.is_empty():
            return 'The linked List is Empty'
        del_element = self.head.element
        self.head = self.head.next
        self.tail.next = self.head
        self.size -= 1
        if self.is_empty():
            self.head = None
            self.tail =None
        return del_element

    def del_last(self):
        if self.is_empty():
            return 'The linked List is Empty'
        thead = self.head
        i = 0
        while i < self.size-2 :
            thead = thead.next
            i += 1
        del_element = thead.element
        thead.next = self.head
        self.tail = thead
        self.size -= 1
        if self.is_empty():
            self.head = None
            self.tail =None
        return del_element

    def del_any(self, pos):
        if self.is_empty():
            return 'The linked List is Empty'
        thead = self.head
        i = 1
        while i < pos-1 :
            thead = thead.next
            i += 1
        del_element = thead.next.element
        thead.next = thead.next.next
        self.size -= 1
        if self.is_empty():
            self.head = None
            self.tail = None
        return del_element

    def display(self):
        thead = self.head
        i = 0
        while i < self.size :
            print(thead.element, end = '-->')
            thead = thead.next
            i += 1
        print()

CL = CircularLinkedList()
CL.add_first(10)
CL.add_first(20)
CL.display()
CL.add_last(50)
CL.add_last(80)
CL.display()
CL.add_any(90,2)
CL.display()
CL.del_first()
CL.display()
CL.del_last()
CL.display()
CL.del_any(1)
CL.display()