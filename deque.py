class Deueue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def show(self):
        print("The queue is :", self.data)

    def add_first(self, element):
        self.data.insert(0, element)
        print("add_first :", element)

    def add_last(self, element):
        self.data.append(element)
        print("add_last :", element)

    def delete_first(self):
        if self.is_empty():
            print("The Dequeue is Empty")
        else:
            value = self.data.pop(0)
            print("Delete First : ", value)

    def delete_last(self):
        if self.is_empty():
            print("The Dequeue is Empty")
        else:
            value = self.data.pop()
            print("Delete last : ", value)


q = Deueue()
q.add_first(10)
q.add_first(20)
q.add_first(30)
q.show()
q.add_last(40)
q.add_last(50)
q.show()
q.delete_first()
q.show()
q.delete_last()
q.show()
