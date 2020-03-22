def enter_operation(a):
    operation = input('Enter operation: ')
    if operation not in a:
        raise ValueError('This is invalid operation')
    return operation

def enter_number():
    number = float(input('Enter number: '))
    return number

def calculate(a, b, c):
    if c == '+':
        return (a + b)
    elif c == '-':
        return (a - b)
    elif c == '*':
        return (a * b)
    elif c == '**':
        return (a ** b)
    elif c == '/':
        try:
            return (a / b)
        except Exception as exc_one:
            print(exc_one, '.', sep='')
            return 'Try again.'