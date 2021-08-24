import operations as o

priority = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2}

number = []
operation = []


def calc(prev_operation):
    global number
    global operation
    x = number.pop()
    y = number.pop()
    if prev_operation[-1] == "+":
        return number.append(o.addition(y, x)), operation.pop()
    elif prev_operation[-1] == "-":
        return number.append(o.subtraction(y, x)), operation.pop()
    elif prev_operation[-1] == "*":
        return number.append(o.multiplication(y, x)), operation.pop()
    elif prev_operation[-1] == "/":
        return number.append(o.division(y, x)), operation.pop()


def main(expression):
    for index, elem in enumerate(expression):
        if elem.isdigit():
            if expression[index - 1].isdigit() and index != 0:
                a = str(number.pop())
                number.append(int(a + elem))
            else:
                number.append(int(elem))
        elif elem == "-" and (index == 0 or expression[index - 1] == "("):
            number.append(-1)
            operation.append("*")
        elif elem == "(":
            operation.append(elem)
        elif elem == ")":
            while priority[operation[-1]] != 0:
                calc(operation[-1])
            else:
                if elem == ")" and operation[-1] == "(":
                    operation.pop()
        elif not operation:
            operation.append(elem)
        elif operation:
            while operation and priority[elem] <= priority[operation[-1]] and len(number) >= 2:
                calc(operation[-1])
            operation.append(elem)
    while operation:
        calc(operation[-1])
    return number[0]


if __name__ == '__main__':
    expression = input("Input your expression:\n").replace(' ', '')
    print(f"Answer: {main(expression)}")
