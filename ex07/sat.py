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


def evaluate(node):

    left_child = ""
    right_child = ""

    if node.data == 0 or node.data == 1:
        return node.data
    elif node.data == "!":
        left_child = evaluate(node.left)
        return not left_child
    else:
        left_child = evaluate(node.left)
        right_child = evaluate(node.right)
    
    if node.data == "|":
        return (left_child | right_child)
    elif node.data == "&":
        return (left_child & right_child)
    elif node.data == "^":
        return (left_child ^ right_child)
    elif node.data == ">":
        return ((not left_child) | right_child)
    elif node.data == "=":
        return (left_child == right_child)
        

def find_combinations(formula):
    
    l = []
    bitwise_l = []

    for char in formula:
        if char.isalpha() and char.isupper() and char not in l:
            l.append(char)

    total_count = 2**len(l)

    for i in range(total_count):
        binary_i = bin(i)[2:]
        if len(binary_i) < len(l):
            binary_i = binary_i.zfill(len(l))

        bitwise_l.append(binary_i)

    return l, bitwise_l


def convert_formula(var, combinations, formula):

    # print(var, combinations, formula)

    formula_dict = []
    for comb in combinations:
        temp_dict = {}
        for i in range(len(comb)):
            temp_dict[var[i]] = comb[i]
        formula_dict.append(temp_dict)
            
    # print(formula_dict)
    converted_formulas = []

    for dict in formula_dict:
        temp_formula = ""
        
        for char in formula:
            if char.isalpha() and char.isupper():
                if char in dict:
                    temp_formula += dict[char]
            else:
                temp_formula += char
        
        converted_formulas.append(temp_formula)

    return converted_formulas


def sat(formula: str)-> bool:

    var, combinations = find_combinations(formula)
    formulas = convert_formula(var, combinations, formula)

    results = []
    for formula in formulas:
        _abs = insert(formula)
        results.append(evaluate(_abs))

    if (True in results):
        return True
    return False



if __name__ == "__main__":

    input = "AA^"

    if check_input(input):
        print(sat(input))
    else:
        print("Error: Wrong formula is invalid!")