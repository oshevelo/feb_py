from Functions import calculate, enter_number, enter_operation

valid_operations = ('+', '-', '*', '/', '**')

try:
    first_number = enter_number()
    second_number = enter_number()
    enter_operation = enter_operation(valid_operations)
except Exception as exc_one:
    print(exc_one, '. Try again.', sep='')
else:
    print(calculate(first_number, second_number, enter_operation))
