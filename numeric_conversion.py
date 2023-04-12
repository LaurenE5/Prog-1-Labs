# Prints decode menu and offers input
def menu():
    choice = input('\nDecoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary'
                   '\n3. Convert binary to hexadecimal\n4. Quit\n \nPlease enter an option: ')
    return choice


# Converts hex code letters to numbers
def hex_char_decode(digit):
    if '0' <= digit <= '9':
        return int(digit)
    elif digit == 'a' or digit == 'A':
        return int(10)
    elif digit == 'b' or digit == 'B':
        return int(11)
    elif digit == 'c' or digit == 'C':
        return int(12)
    elif digit == 'd' or digit == 'D':
        return int(13)
    elif digit == 'e' or digit == 'E':
        return int(14)
    elif digit == 'f' or digit == 'F':
        return int(15)
    else:
        return 'Invalid code'


# Converts hex string
def hex_string_decode(hex):
    # Gets rid of the 0x when hex code gets input
    if hex[0] == '0' and hex[1] == 'x':
        hex = hex[2:]
    left_most_bit_index = len(hex) - 1
    res = 0
    # converts hex code to decimal value
    for digit in hex:
        res += hex_char_decode(digit) * (16 ** left_most_bit_index)
        left_most_bit_index -= 1
    return res


# Decodes binary string
def binary_string_decode(bin):
    # gets rid of 0b when inputting binary code
    if bin[0] == '0' and bin[1] == 'b':
        bin = bin[2:]
    left_most_bit_index = len(bin) - 1
    res = 0
    # converts binary code to decimal value
    for binary in bin:
        res += int(binary) * (2 ** left_most_bit_index)
        left_most_bit_index -= 1
    return res


# converts binary string to hex code
def binary_to_hex(binary):
    decimal = binary_string_decode(binary)
    power = 2
    list = ''
    while decimal >= 16:
        while decimal >= 16 ** power:
            power += 1
        power -= 1
        value = decimal // 16 ** power
        decimal -= ((16 ** power) * value)
        # converts value to hex letters
        if 0 <= value <= 9:
            code = str(value)
        elif value == 10:
            code = 'A'
        elif value == 11:
            code = 'B'
        elif value == 12:
            code = 'C'
        elif value == 13:
            code = 'D'
        elif value == 14:
            code = 'E'
        elif value == 15:
            code = 'F'
        list += code
    # converts value to letters
    if 0 <= decimal <= 9:
        code = str(decimal)
    elif decimal == 10:
        code = 'A'
    elif decimal == 11:
        code = 'B'
    elif decimal == 12:
        code = 'C'
    elif decimal == 13:
        code = 'D'
    elif decimal == 14:
        code = 'E'
    elif decimal == 15:
        code = 'F'
    list += code
    return list


def main():
    decode = True
    # keeps programming running
    while decode:
        choice = int(menu())

        # menu options

        # decodes hexadecimal
        if choice == 1:
            hex = input('Please enter the numeric string to convert: ')
            res = hex_string_decode(hex)
            # prints the result of hex string as decimal value
            print('Result: ', res)

        # decodes binary
        elif choice == 2:
            bin = input('Please enter the numeric string to convert: ')
            res = binary_string_decode(bin)
            # prints the result of binary string as decimal value
            print('Result:', res)

        # converts binary to hexadecimal
        elif choice == 3:
            binary = input('Please enter the numeric string to convert: ')
            list = binary_to_hex(binary)
            # prints the binary string as a hex value
            print('Result: ', list)

        # ends the program
        else:
            print('Goodbye!')
            break

if __name__ == '__main__':
    main()
