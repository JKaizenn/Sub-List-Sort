
def getNumber():
    number = -1
    while True:
        try:
            number = int(input("Enter a positive integer: "))
            if number >= 0:
                return number
            print("Please enter a positive number (>0):")
            if number <0:
                raise ValueError
        except ValueError:
            print("Invalid Number, Please input a valid number")

def getFormat():
    options = {'hex','bin','oct','all'}
    selection = ''
    while selection.lower() not in options:
        selection = input(f"Please enter a format of Hex, Bin, Oct, or All {options}:")
    return selection.lower()


def display(number,conversions, format):
    print(f'{number},{conversions},{format}')

def convert(number):
    bin = convert_to_binary(number)
    oct = convert_to_octal(number)
    hex = convert_to_hex(number)

    return oct, bin, hex

def convert_to_binary(number):
    """Convert an integer number to binary. Return the binary string representation of the number"""
    binary_digits = []
    while number > 0:
        binary_digits.append(number %2)
        number //= 2
        print(binary_digits)
    binary_string = ''
    for i in range(len(binary_digits)-1,-1,-1):
        binary_string += str(binary_digits[i])
        
        print(binary_string)
  
  
def convert_to_octal(number):
    return oct(number)[2:]

def convert_to_hex(number):
    return hex(number)[2:]


def get_test_number():
    number = -1
    while number != 0:
        number = getNumber()
        number = get_number()
        
        
def main():
    
    number = getNumber()
    format = getFormat()
    conversions = convert(number)
    display(number, conversions, format)

if __name__ == "__main__":
    main()