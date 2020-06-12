
#
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.last = 0

    def append(self, x):
        if len(self.data) < self.capacity:
            self.data.append(x)
        else:
            self.data[self.last] = x
            if self.last < len(self.data) - 1:
                self.last += 1
            else:
                self.last = 0

    def get(self):
        return self.data
