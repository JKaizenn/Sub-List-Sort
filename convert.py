
def getNumber():
    return 0


def getFormat():
    return 'all'


def display(number, format):
    print(f'{number}, {format}')

def convert(number):
    bin = convert_to_binary(number)
    oct = convert_to_octal(number)
    hex = convert_to_hex(number)

    return oct, bin, hex

def convert_to_binary(number):
    return "0101"
  
def convert_to_octal(number):
    return "71"

def convert_to_hex(number):
    return "A"  

def main():
    
    number = getNumber
    format = getFormat
    
    conversions = convert(number)
    
    # print(number,format)
    display(conversions, format)

main()