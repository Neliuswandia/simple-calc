def simple_calc():

    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    operation = input('Enter operation (+,-,/,*):').strip()

    if operation == '+':
        result = num1 + num2

    elif operation =='-':
        result = num1 - num2

    elif operation =='/':
        result = num1 / num2

    elif operation =='*':
        result = num1 * num2

    else :
        result = "invalid operation"

    print(f'Result: {result}')

simple_calc()

