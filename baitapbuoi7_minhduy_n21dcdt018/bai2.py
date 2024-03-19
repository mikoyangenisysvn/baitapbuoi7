class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        value = self.list[::-1]  # Reverse the list without modifying it
        value = [str(x) for x in value]
        return '\n'.join(value)

    def isEmpty(self):  # Corrected method name
        return self.list == []

    def push(self, value):  # Moved the method inside the class
        self.list.append(value)
        return "The element has been successfully inserted"

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
