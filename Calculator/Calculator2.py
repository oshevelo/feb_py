from Functions import calculate, enter_operation, enter_number

valid_operations = ('+', '-', '*', '/', '**')

try:
    first_numb = enter_number()
    first_operation = enter_operation(valid_operations)
    second_numb = enter_number()
    second_operation = enter_operation(valid_operations)
    third_numb = enter_number()
except Exception as exc_one:
    print(exc_one, '. Try again.', sep='')
else:
    try:
        print(calculate(calculate(first_numb, second_numb, first_operation), third_numb, second_operation))
    except:
        print('Try again.')