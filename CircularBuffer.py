class CircularBuffer:
    array = []
    size = 0
    idx = 0

    def __init__(self, size):
        self.array = [[] for _ in range(0, size)]
        self.size = size

    def push(self, x):
        self.array[self.idx] = x
        self.idx = (self.idx + 1) % self.size

    def get_ordered(self):
        retarr = []
        for i in range(0, self.size):
            retarr += [self.rray[(i + self.idx) % self.size]]
        return retarr


buf = CircularBuffer(2)

buf.push(1)
buf.push(2)
buf.push(3)

for n in buf.get_ordered():
    print(n)
