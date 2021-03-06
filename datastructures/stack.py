class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1
        self.__values = []

    def is_empty(self):
        if self.__top == -1:
            return True

    def length(self):
        return self.__top + 1

    def is_capacity_max(self):
        if self.__top == self.__capacity - 1:
            return True

        return False

    def insert(self, value):
        if self.is_capacity_max():
            print("Capacidade máxima atiginda")
        else:
            self.__top += 1
            self.__values.append(value)

    def remove(self):
        value = self.__values[self.__top]
        self.__top -= 1

        return value

    def peek(self):
        if self.__top != -1:
            return self.__values[self.__top]

        return ""
