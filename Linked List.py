class LinkedList :
    class Node :
        __slots__ =  'element' , 'next'
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
        return  self.size == 0

    def add_first(self, e):
        newest = self.Node(e, None)
        if self.is_empty() :
            self.head = newest
            self.tail = newest
        else :
            newest.next = self.head
        self.head = newest
        self.size += 1

    def add_last(self, e):
        newest = self.Node(e, None)
        if self.is_empty():
            self.head = newest
            self.tail = newest
        else :
            self.tail.next = newest
        self.tail = newest
        self.size += 1

    def add_any(self, e, pos):
        newest = self.Node(e, None)
        thead = self.head
        i = 1
        while i < pos :
            thead = thead.next
            i += 1
        newest.next = thead.next
        thead.next = newest
        self.size += 1

    def del_first(self):
        if self.is_empty():
            return 'The linked list is Empty.'
        del_element = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.head = None
            self.tail = None
        return del_element

    def del_last(self):
        if self.is_empty():
            return 'The Linked List is Empty'
        thead = self.head
        i = 0
        while i < self.size-2 :
            thead = thead.next
            i += 1
        del_element = self.tail.element
        self.tail = thead
        self.tail.next = None
        self.size -= 1
        if self.is_empty():
            self.head = None
            self.tail = None
        return del_element

    def del_any(self, pos):
        if self.is_empty():
            return 'The Linked List is Empty'
        if pos == 0:
            self.del_first()
            return 0
        thead = self.head
        i = 1
        while i < pos-1 :
            thead = thead.next
            i += 1
        del_element = thead.next.element
        thead.next = thead.next.next
        self.size -= 1
        return del_element

    def display(self):
        thead = self.head
        while thead :
            print(thead.element, end = "-->")
            thead = thead.next
        print()

L = LinkedList()
L.add_first(10)
L.add_first(20)
L.add_first(60)
L.add_first(50)
L.display()
L.add_last(90)
L.add_last(777)
L.display()
L.add_any(40,3)
L.display()
L.del_first()
L.display()
L.del_last()
L.display()
L.del_any(1)
L.display()