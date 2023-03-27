class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, value):
        self.headValue = Node(value)
        self.tailValue = Node(value)
        self.length = 1

    def insertFromEnd(self, value):
        newNode = Node(value)
        self.tailValue.next = newNode
        self.tailValue =newNode
        self.length += 1

        return self

    def remove_nth_node_from_end(self, index):
        pointerNode = self.headValue
        count = 1
        while pointerNode:
            count += 1
            pointerNode.next

        currentNode = previousNode = self.headValue
        for i in range(self.length-index):
            previousNode = currentNode
            currentNode = currentNode.next
        previousNode.next = currentNode.next
        currentNode.next =None

        return self
            

    def printLinkedList(self):
        pointer = self.headValue
        finalList = ''
        while pointer:
           
                finalList += str(pointer.data) + '-->'
                pointer = pointer.next
                print(finalList)

head = LinkedList(3)
head.insertFromEnd(4)
head.insertFromEnd(5)
head.insertFromEnd(6)
head.printLinkedList()
