class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

    
def insert(input):
    stack = []

    for d in input:
        
        if d.isdigit():
            stack.append(Node(int(d)))

        elif d == "!":
            node = Node(d)
            node.left = stack.pop()
            stack.append(node)

        else:
            right = stack.pop()
            left = stack.pop()

            node = Node(d)
            node.right = right
            node.left = left

            stack.append(node)

    return stack[0]
