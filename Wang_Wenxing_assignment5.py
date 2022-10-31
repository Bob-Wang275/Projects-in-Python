# I use Stack to complete a simple application that can evaluate an arithmetic expression to compute the value.
# The operations only include +, -, * and /.

from Stack import Stack


def isBlanced(expression):
    s_brace = Stack()
    for k in expression:
        if k == '{' or k == '[' or k == '(':
            s_brace.push(k)  # Push every bracket's left part into the stack.
        elif k == ')' or k == ']' or k == '}':
            if (k == ')' and s_brace.top() == '(') or (k == '}' and s_brace.top() == '{') or (k == ']' and s_brace.top() == '['):
                s_brace.pop()  # Check if the next right part match the top of stack. If match, pop.
            else:
                return False  # If not match, imbalanced.
    if s_brace.isEmpty():
        return True  # If every left part pop from stack, balanced.
    else:
        return False  # If stack still have left parts, imbalanced.


def query(in_put):  # Accept the user's input and deal.
    while True:
        if in_put == "Y" or in_put == "y":
            return True
        elif in_put == "N" or in_put == "n":
            return False
        else:
            in_put = input("Invalid Response. Please type Y or N.")


def evaluate(expression):
    numbers = Stack()
    operation = Stack()
    length = len(expression)  # Get the length of expression.
    number = ''
    i = 0
    while i < length:
        if expression[i].isdigit():   # Deal with the number of expression.
            number = number + expression[i]
            if i < length-1:
                i = i + 1
                while expression[i].isdigit():
                    number = number + expression[i]
                    if i < length - 1:
                        i = i + 1
                    else:
                        break
                i = i - 1
            numbers.push(number)
            number = ''
        elif expression[i] == '+' or expression[i] == '-' or expression[i] == '/' or expression[i] == '*':  # Deal with '+-*/' of expression.
            operation.push(expression[i])
        elif expression[i] == '.':
            number = numbers.pop() + '.'  # Deal with decimal of expression.
            if i < length-1:
                i = i + 1
                while expression[i].isdigit():
                    number = number + expression[i]
                    if i < length-1:
                        i = i + 1
                    else:
                        break
                i = i - 1
            numbers.push(number)
            number = ''
        elif expression[i] == '{' or expression[i] == '[' or expression[i] == '(':
            pass
        elif expression[i] == '}' or expression[i] == ']' or expression[i] == ')':
            #  evaluateStackTops(numbers, operation) Call evaluateStackTops for compute.
            if evaluateStackTops(numbers, operation) == -1:
                return -1
        else:
            print("The Expression is Illegal.")
            return -1
        print(expression[i])
        i = i + 1
    return round(numbers.top(), 2)


def evaluateStackTops(numbers, operation):  # Compute with two numbers and on operation.
    if numbers.isEmpty():
        print("The Expression is Illegal1.")
        return -1
    operand2 = float(numbers.pop())
    print(operand2)
    if numbers.isEmpty():
        print("The Expression is Illegal2.")
        return -1
    operand1 = float(numbers.pop())
    print(operand1)
    if operation.isEmpty():
        print("The Expression is Illegal3")
        return -1
    operation_using = operation.pop()
    if operation_using == '+':
        numbers.push(operand1+operand2)
    elif operation_using == '-':
        numbers.push(operand1-operand2)
    elif operation_using == '*':
        numbers.push(operand1*operand2)
    elif operation_using == '/':
        numbers.push(operand1/operand2)
    return numbers.top()


def main():
    print("Please type an arithmetic expression made from")
    print("unsigned numbers and the operations + - * /.")
    print("The expression must be fully parenthesized.")
    while True:
        expression = input("Your expression: ")
        if isBlanced(expression):
            if evaluate(expression) != -1:
                print("The value is", evaluate(expression))
        else:
            print("That is not balanced.")
        user_y_n = input("Another String? [Y or N]:")
        if not query(user_y_n):
            break
    print("All numbers are interesting.")


if __name__ == "__main__":
    main()
