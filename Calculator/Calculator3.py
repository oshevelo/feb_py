from math import pi, e
from Functions import enter_operation, enter_number

valid_operations = ('+', '-', '*', '/', '**')
try:
    first_number = input('Enter number or Constant (pi, e): ')
    first_operation = enter_operation(valid_operations)
    second_number = input('Enter number or Constant (pi, e): ')
    second_operation = enter_operation(valid_operations)
    third_number = input('Enter number or Constant (pi, e): ')
except Exception as exc_one:
    print(exc_one, '. Try again.', sep='')
else:
    try:
        first_number = str(first_number)
        second_number = str(second_number)
        third_number = str(third_number)
        print(eval(first_number + first_operation + second_number + second_operation + third_number))
    except ZeroDivisionError:
        print('Error. Division by zero. Try again.')
    except Exception as exc_two:
        print('Entered wrong value. Enter number or Constant (pi, e).', sep='')