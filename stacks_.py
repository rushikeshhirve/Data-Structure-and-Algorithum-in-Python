class Stacks :
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0
    def __len__(self):
        return len(self.data)
    def push(self, data):
        self.data.append(data)
    def pop(self):
        if self.is_empty():
            return 'The stack is Empty'
        else :
            return self.data.pop()
    def top(self):
        if self.is_empty():
            return 'The stack is Empty'
        else :
            return self.data[-1]

s = Stacks()
s.push(10)
s.push(20)
print(s.data)
print('Length : ', s.__len__())
print('Poped : ', s.pop())
s.push(30)
print(s.data)


