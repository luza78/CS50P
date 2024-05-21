class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        if self.size > 0:
            return "🍪" * self.size
        else:
            return ""

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("capacity Exceeded")
        self.size = self.size + n

    def withdraw(self, size):
        if self.size >= size:
            self.size = self.size - size
        else:
            raise ValueError("not enough cookies")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        try:
            if int(capacity) > 0:
                self._capacity = capacity
            else:
                raise ValueError()
        except ValueError:
            raise ValueError("bad value for capacity")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size <= self.capacity:
            self._size = size
        else:
            raise ValueError("size cannot exceed capacity")


def main():
    ...


if __name__ == "__main__":
    main()
