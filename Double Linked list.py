class DoubleLinkedList :
    class Node :
        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
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
        newest = self.Node(e, None, None)
        if self.is_empty():
            self.head = newest
            self.tail = newest
        else :
            newest.next = self.head
            self.head.prev = newest
        self.head = newest
        self.size += 1

    def add_last(self, e):
        newest = self.Node(e, None, None)
        if self.is_empty():
            self.head = newest
            self.tail = newest
        else:
            self.tail.next = newest
            newest.prev = self.tail
        self.tail = newest
        self.size += 1

    def add_any(self, e, pos):
        newest = self.Node(e, None, None)
        thead = self.head
        i = 1
        while i< pos :
            thead = thead.next
            i += 1
        newest.next = thead.next
        newest.prev = thead
        thead.next.prev = newest
        thead.next = newest
        self.size += 1

    def del_first(self):
        if self.is_empty():
            return 'The linked List is Empty'
        del_element = self.head.element
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        if self.is_empty():
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
        del_element = self.tail.element
        self.tail = thead
        # self.tail.next = None
        self.size -= 1
        if self.is_empty():
            self.tail =None
        return del_element

    # def del_last(self):
    #     if self.is_empty():
    #         return 'The linked List is Empty'
    #     del_element = self.tail.element
    #     self.tail = self.tail.prev
    #     self.tail.next = None
    #     self.size -= 1
    #     return del_element


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
        thead.next.next.prev = thead
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

DL = DoubleLinkedList()
DL.add_first(10)
DL.add_first(20)
DL.display()
DL.add_last(50)
DL.add_last(80)
DL.display()
DL.add_any(90,2)
DL.display()
DL.del_first()
DL.display()
DL.del_last()
DL.display()
DL.del_any(1)
DL.display()