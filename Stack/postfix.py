from Stack import Stack


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def postfix(stack_reversed):
    stack = Stack()

    el = stack_reversed.pop()
    while el is not None:
        if isinstance(el, int):
            stack.push(el)
        elif el == "=":
            return stack.pop()
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if el == "+":
                operation = add
            elif el == "*":
                operation = multiply
            elif el == "-":
                operation = minus
            elif el == "/":
                operation = divide
            stack.push(operation(num1, num2))
        el = stack_reversed.pop()

    return None
