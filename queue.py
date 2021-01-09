class Queue :
    def __init__(self):
        self.data = []
        self.size = 0
        self.front = 0

    def enqueue(self, e):
        self.data.append(e)
        self.size += 1

    def dequeue(self):
        if self.size == 0 :
            print('The queue is empty.')
        else:
            value = self.data[self.front]
            self.data[self.front] = None
            self.front -= 1
            self.size -= 1
        return value

    def first(self):
        return self.data[self.front]

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.data)
print(q.size)
q.dequeue()
print(q.data)
print(q.size)
print(q.first())
q.enqueue(30)
q.enqueue(40)
print(q.data)