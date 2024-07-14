from Stack import Stack


def balancedBrackets(string: str) -> bool:
    s = Stack()
    for i in string:
        if i == "(":
            s.push(i)
        if i == ")":
            if s.size() == 0:
                return False
            s.pop()

    return s.size() == 0
