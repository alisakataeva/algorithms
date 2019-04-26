

class Array:

    def __init__(self, size, type):
        self.type = type
        self.memory = []
        self.length = 0

    def __addingValidation(self, element):

        if type(element) != self.type:
            raise TypeError("Error : New element must have '{type}' type."
                .format(self.type))

        if self.length == len(self.memory):
            raise Exception("Error : Can not add item => No space available.")

    def __removingValidation(self):

        if self.memory == [] or self.length < 1:
            raise Exception("Error : Can not remove item => Array is empty.")

    def push(self, element):

        self.__addingValidation(element)

        self.memory[self.length] = element
        self.length += 1

    def pop(self):

        self.__removingValidation()

        del self.memory[self.length-1]
        self.length -= 1

    def unshift(self, element):

        self.__addingValidation(element)

        current = element
        for i in range(self.length):
            previous = self.memory[i]
            self.memory[i] = current
            current = previous

        self.memory[self.length] = current
        self.length += 1

    def shift(self):

        self.__removingValidation()

        for i in range(self.length):
            try:
                self.memory[i] = self.memory[i+1]
            except IndexError:
                pass

        del self.memory[self.length-1]
        self.length -= 1