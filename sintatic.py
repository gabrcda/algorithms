OPEN = "({[<"
CLOSE = ")}]>"
MATCH = {")":"(", "}":"{", "]":"[", ">":"<"}

def get_expression():
    return input("Expression: ")

def analyse(expression):
    stack = []
    for term in expression:
        if term in OPEN:
            stack.append(term)
        elif term in CLOSE:
            if MATCH[term] == stack[-1]:
                stack.pop()
    
    return stack

if __name__ == "__main__":
    expression = get_expression()
    if len(analyse(expression)) == 0:
        print("valid expression!")
    else:
        print("invalid expression!")