class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


def traversingALinkedList(head):
    currNode = head
    while currNode:
        print(currNode.data, end="->")
        currNode = currNode.next
    print("null")

def insertAtNode(head, newNode, position):
    if(position == 1):
        newNode.next = head
        return newNode
    
    currentNode = head

    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next
    
    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

node1 = Node(7)
node2 = Node(4)
node3 = Node(1)
node4 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node4

traversingALinkedList(node1)

# Inserting a new node
newNode = Node(100)
node1 = insertAtNode(node1, newNode, 2)

traversingALinkedList(node1)