class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.first = None

    def addNode(self, value):
        node = Node(value)
        if self.first:
            cur_node = self.first
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = node
        else:
            self.first = node
        return node

    def removeNode(self, value):
        pass

    def getNode(self, ind):
        cur_ind = 0
        cur_node = self.first
        while cur_ind <= ind:
            if cur_ind == ind:
                break
            elif cur_node.next:
                cur_node = cur_node.next
            else:
                cur_node = None
                break
            cur_ind +=1
        return cur_node

    def findNode(self, value):
        cur_node = self.first
        while cur_node:
            if cur_node.value == value:
                break
            if cur_node.next:
                cur_node = cur_node.next
            else:
                cur_node = None

        if cur_node:
            return cur_node
        return None

class Array:

    def __init__(self):
        self.list = []
        self.length = 0

    def addElem(self, value):
        self.list.append(value)
        self.length +=1
        return (self.length-1, value)

    def getElem(self, ind):
        try:
            return self.list[ind]
        except IndexError:
            return None

    def findElem(self, value):
        for (i, el) in enumerate(self.list):
            if el == value:
                return i, el
        return None