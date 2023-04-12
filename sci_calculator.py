import math

display_menu = True
sum = 0.0

# Current result
result = 0.0
print('Current Result: ', result)

# Calculator Menu
print('Calculator Menu')
print('---------------')
print('0. Exit Program')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Exponentiation')
print('6. Logarithm')
print('7. Display Average')

count = 0
option = float(input("Enter Menu Selection: "))

# Calculator Operations
while option != 0:
    if count != 0 and option == 7:
        print('Current Result: ', num_4)
        print('Calculator Menu')
        print('---------------')
        print('0. Exit Program')
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        print('5. Exponentiation')
        print('6. Logarithm')
        print('7. Display Average')

        option = float(input("Enter Menu Selection: \n"))

    # Not Menu Option
    if option > 7 or option < 0:
        print('Error: Invalid selection!')
        option = float(input("Enter Menu Selection: \n"))

    if option > -1:

        # Addition

        if option == 1:
            num_1 = input('Enter first operand: ')
            if input == 'RESULT!':
                num_1 = result
            num_2 = input('Enter second operand: ')
            if input == 'RESULT!':
                num_2 = result
            num_4 = float(num_1) + float(num_2)
            result = num_4
            print()
            count += 1
            sum += num_4
            option = 7

        # Subtraction

        elif option == 2:
            num_1 = input('Enter first operand: ')
            if input == 'RESULT!':
                num_1 = result
            num_2 = input('Enter second operand: ')
            if input == 'RESULT!':
                num_2 = result
            num_4 = float(num_1) - float(num_2)
            result = num_4
            print()
            count += 1
            sum += num_4
            option = 7

        # Multiplication

        elif option == 3:
            num_1 = input('Enter first operand: ')
            if input == 'RESULT!':
                num_1 = result
            num_2 = input('Enter second operand: ')
            if input == 'RESULT!':
                num_2 = result
            num_4 = float(num_1) * float(num_2)
            result = num_4
            print()
            count += 1
            sum += num_4
            option = 7

        # Division

        elif option == 4:
            num_1 = input('Enter first operand: ')
            if input == 'RESULT!':
                num_1 = result
            num_2 = input('Enter second operand: ')
            if input == 'RESULT!':
                num_2 = result
            num_4 = float(num_1) / float(num_2)
            result = num_4
            print()
            count += 1
            sum += num_4
            option = 7

        # Exponentials

        elif option == 5:
            num_1 = input('Enter first operand: ')
            if input == 'RESULT!':
                num_1 = result
            num_2 = input('Enter second operand: ')
            print()
            if num_2 == 'RESULT!':
                num_2 = result
            num_4 = float(num_1) ** float(num_2)
            result = num_4
            print()
            count += 1
            sum += num_4
            option = 7

        # Logarithms

        elif option == 6:
            num_1 = input('Enter first operand: ')
            if input == 'RESULT!':
                num_1 = result
            num_2 = input('Enter second operand: ')
            if input == 'RESULT!':
                num_2 = result
            num_4 = math.log(float(num_2), float(num_1))
            result = num_4
            print()
            count += 1
            sum += num_4
            option = 7

        # Average

        elif option == 7:
            if count == 0.0:
                print('Error: No calculations yet to average!')
                print()
            elif count > 0.0:
                print('Sum of calculations: ', str(sum))
                print('Number of calculations: ', str(count))
                num_5 = round((sum/count), 2)
                num_5 = str(num_5)
                print('Average of calculations: ', num_5)
            option = float(input('Enter Menu Selection: '))

# Exit Program

if option == 0:
    display_menu = False
    print('Thanks for using this calculator. Goodbye!')
