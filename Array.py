class Array:
    def __init__(self, size: int):
        self.size = size
        self.array = []
        self.len = 0

    def length_increase(self):
        self.len += 1

    def insert(self, item):
        if self.len == self.size:
            print('array is full')
            new_array = Array(self.len + 1)
            for i in self.array:
                new_array.array.append(i)
            self.array.clear()
            new_array.array.append(item)
            self.length_increase()
            self.array = new_array.array
        else:
            self.array.append(item)
            self.length_increase()
        return self.array

    def max(self):
        maximum = self.array[0]
        for i in range(1, len(self.array)):
            if self.array[i] > maximum:
                maximum = self.array[i]
        return f"max number is {maximum}"

    def insert_at(self, item):
        pass

    def reverse(self):
        reversed_array = []
        for i in self.array[::-1]:
            reversed_array.append(i)
        return reversed_array

    def remove_at(self, index: int):
        if 0 > index or index >= self.len:
            raise ValueError('index out of range')
        elif index == self.len:
            self.array.pop()
            self.len -= 1
        else:
            for i in range(index, self.len - 1):
                self.array[i] = self.array[i + 1]
            self.array.pop()
            self.len -= 1
        return self.array

    def index_of(self, item):
        for i in range(len(self.array)):
            if item == i:
                return item
        else:
            return -1

    def print(self):
        for i in self.array:
            print(i)


array = Array(3)
array.insert(10)
array.insert(20)
array.insert(30)
array.insert(40)
array.insert(50)
array.remove_at(2)
print(array.max())
print(array.reverse())
array.print()
