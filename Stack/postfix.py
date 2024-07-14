from Stack import Stack


def postfix(stack_reversed):
    stack = Stack()

    el = stack_reversed.pop()
    while el is not None:
        if isinstance(el, int):
            stack.push(el)
        elif el == "+":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.push(num1 + num2)
        elif el == "*":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.push(num1 * num2)
        elif el == "=":
            return stack.pop()
        el = stack_reversed.pop()
