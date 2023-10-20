

result = None
operand = None
operator = None
wait_for_number = True

#here me
while True:
    value = input('>>>>>')
    
    try:
        if result is None:
            result = int(value)
            wait_for_number= False
            print('result')
        elif not wait_for_number and  value != '=':
            if value in ['+','-','*','/']:
                operator= value
                wait_for_number = True
            else:
                print('need operator')
            print('operator')
        elif wait_for_number:
            operand = int(value)
            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '*':
                result *= operand
            elif operator == '/':
                result /= operand
            wait_for_number = False

            print('number')
        elif value == '=':
            
            print(f'Result: {result}')
            break

    except ValueError:
        print('The number')
    except TypeError:
        print('incorrect input')
    except ZeroDivisionError:
        print("Don't enter 0")
       