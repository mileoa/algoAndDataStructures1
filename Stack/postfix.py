from Stack import Stack


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
                stack.push(num1 + num2)
            elif el == "*":
                stack.push(num1 * num2)
            elif el == "-":
                stack.push(num1 - num2)
            elif el == "/":
                stack.push(num1 / num2)
        el = stack_reversed.pop()

    return None
