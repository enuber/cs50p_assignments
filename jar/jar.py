class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if int(n) > self._capacity or int(n) + self._size > self.capacity:
            raise ValueError
        self._size += int(n)

    def withdraw(self, n):
        if int(n) > self._size:
            raise ValueError
        self._size -= int(n)

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if int(size) > self._capacity:
            raise ValueError
        self._size = size


def main():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(4)
    print(jar.capacity)
    print(jar.size)

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/jar
