from abs import Node, insert

def check_input(input: str) -> bool:

    boolean = 0
    expression = 0

    for char in input:
        if char.isalpha() and char.isupper():
            boolean += 1
        elif char == "&" or char == "|" or char == "^" or char == ">" or char == "=":
            expression += 1

    if (expression+1) == boolean:
        return True
    return False


def postorder(node, res):
    
    if node is None:
        return
    
    postorder(node.left, res)
    postorder(node.right, res)

    res.append(node.data)


def conv_nnf(node):
    
    if node.data.isalpha():
        return node

    elif node.data == "&" or node.data == "|":
        
        node.left = conv_nnf(node.left)
        node.right = conv_nnf(node.right)

        return node
        
    elif node.data == ">":
        # Rule2: Material conditions
        
        root = Node("|")
        root.left = Node("!")
        root.left.left = node.left
        root.right = node.right

        return conv_nnf(root)
    
    elif node.data == "=":
        # Rule3: Equivalence

        # AB= -> (A&B) | (!A&!B)

        root = Node("|")
        root.left = Node("&")
        root.right = Node("&")

        root.left.left = node.left
        root.left.right = node.right

        root.right.left = Node("!")
        root.right.left.left = node.left
        root.right.right = Node("!")
        root.right.right.left = node.right

        return (conv_nnf(root))


    elif node.data == "!":
        if node.left.data.isalpha():
            return node # this case okay eg !A
        elif node.left.data == "!":
            # Rule1: Elimination of double negation
            return node.left.left
        
        elif node.left.data == "&":
            # Rule4: De Morgan's laws AND
            
            root = Node("|")
            root.left = Node("!")
            root.right = Node("!")
            root.left.left = node.left.left
            root.right.left = node.left.right

            return conv_nnf(root)

        elif node.left.data == "|":
            # Rule4: De Morgan's laws OR
            
            root = Node("&")
            root.left = Node("!")
            root.right = Node("!")
            root.left.left = node.left.left
            root.right.left = node.left.right

            return conv_nnf(root)

    return node

# idea is | node's child can't be & that's why use Rule 5: Distributivity
# (A ∨ (B ∧ C)) ⇔ ((A ∨ B) ∧ (A ∨ C)) or (A | (B & C)) = ((A | B) & (A | C))
def conv_cnf(node):

    if node.data.isalpha() or node.data == "!":
        return node
    
    elif node.data == "&":
        node.left = conv_cnf(node.left)
        node.right = conv_cnf(node.right)

        return node
    
    elif node.data == "|":

        node.left = conv_cnf(node.left)
        node.right = conv_cnf(node.right)

        if node.left.data == "&":
            # (A & B) | C → (A|C) & (B|C)
            root = Node("&")
            root.left = Node("|")
            root.right = Node("|")

            root.left.left = node.left.left
            root.left.right = node.right

            root.right.left = node.left.right
            root.right.right = node.right

            return conv_cnf(root)
        
        if node.right.data == "&":
            # A | (B & C) → (A|B) & (A|C)

            root = Node("&")
            root.left = Node("|")
            root.right = Node("|")

            root.left.left = node.left
            root.left.right = node.right.left

            root.right.left = node.left
            root.right.right = node.right.right

            return conv_cnf(root)

        return node

    return node
    

# cnf = "!" only can be only with variables not operations. & must be only in last(top) and | comes before than &.
# solution: first implement nnf, second implement rule 5(distribute or).
def conjunctive_normal_form(formula: str)-> bool:

    _abs = insert(formula)
    _abs = conv_nnf(_abs)
    _abs = conv_cnf(_abs)
    
    result = []
    postorder(_abs, result)

    res = ""
    for i in result: res += i

    return res



if __name__ == "__main__":

    input = "AB|!C!&"

    if check_input(input):
        print(conjunctive_normal_form(input))
    else:
        print("Error: Wrong formula is invalid!")