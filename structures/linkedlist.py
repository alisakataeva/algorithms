

class Node:

    def __init__(self, element):
        self.element = element
        self.prev = None
        self.next = None


class Base:

    def __init__(self):
        self.length = 0
        self.top = None

    def push(self, element):
        """ override this """
        pass

    def pop(self):
        """ override this """
        pass

    def unshift(self, element):
        """ override this """
        pass

    def shift(self):
        """ override this """
        pass

    def addAt(self, index):
        """ override this """
        pass

    def removeAt(self, index):
        """ override this """
        pass

    def isEmpty(self):
        return self.length == 0

    def indexOf(self, element):
        pass

    def elementAt(self, index):
        pass

    def _decrementLength(self):
        if self.length > 0:
            self.length -= 1
        else:
            self.length = 0

    def _incrementLength(self):
        self.length += 1


class LinkedList(Base):

    def push(self, element):
        node = Node(element)
        if not self.top:
            self.top = node
        else:
            last = self.top
            while last.next:
                last = last.next
            last.next = node
        self._incrementLength()

    def pop(self):
        if not self.top:
            pass
        else:
            current = self.top
            previous = self.top
            while current.next:
                previous = current
                current = current.next
            if (current == previous):
                self.top = None
            else:
                previous.next = None
        self._decrementLength()

    def unshift(self, element):
        node = Node(element)
        if not self.top:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self._incrementLength()

    def shift(self):
        if not self.top:
            pass
        elif not self.top.next:
            self.top = None
        else:
            self.top = self.top.next
        self._decrementLength()


class DoublyLinkedList(Base):

    def __init__(self):
        super().__init__()
        self.last = None

    def push(self, element):
        node = Node(element)
        if not self.top:
            self.top = node
            self.last = node
        else:
            node.prev = self.last
            self.last.next = node
        self._incrementLength()

    def pop(self, element):
        if not self.top:
            pass
        elif self.top == self.last:
            self.top = None
            self.last = None
        else:
            self.last = self.last.prev
            self.last = None
        self._decrementLength()

    def unshift(self, element):
        node = Node(element)
        if not self.top:
            self.top = node
            self.last = node
        else:
            self.top.prev = node
            node.next = self.top
            self.top = node
        self._incrementLength()

    def shift(self):
        if not self.top:
            pass
        elif self.top == self.last:
            self.top = None
            self.last = None
        else:
            self.top = self.top.next
            self.top.prev = None
        self._decrementLength()