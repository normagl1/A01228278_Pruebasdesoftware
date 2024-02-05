import sys
import time

def convert_to_binary(number):
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary if binary else '0'

def convert_to_hexadecimal(number):
    hexadecimal = ''
    hex_chars = '0123456789ABCDEF'
    while number > 0:
        hexadecimal = hex_chars[number % 16] + hexadecimal
        number = number // 16
    return hexadecimal if hexadecimal else '0'

def process_file(file_path):
    start_time = time.time()
    try:
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        sys.exit(1)

    results = "Number\tBinary\tHexadecimal\n"
    for number in numbers:
        binary = convert_to_binary(number)
        hexadecimal = convert_to_hexadecimal(number)
        results += f"{number}\t{binary}\t{hexadecimal}\n"

    elapsed_time = time.time() - start_time
    results += f"\nElapsed Time: {elapsed_time} seconds"

    print(results)
    with open("ConversionResults.txt", "w") as file:
        file.write(results)

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("To convert a single number to binary: python convertNumbers.py binary <number>")
        print("To convert a single number to hexadecimal: python convertNumbers.py hex <number>")
        print("To process a file: python convertNumbers.py file <filepath>")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "file":
        if len(sys.argv) != 3:
            print("Usage for file mode: python convertNumbers.py file <filepath>")
            sys.exit(1)
        process_file(sys.argv[2])
    else:
        if len(sys.argv) != 3 or not sys.argv[2].isdigit():
            print("Invalid number. Please provide a valid integer.")
            sys.exit(1)
        number = int(sys.argv[2])
        if mode == "binary":
            print(f"Binary: {convert_to_binary(number)}")
        elif mode == "hex":
            print(f"Hexadecimal: {convert_to_hexadecimal(number)}")
        else:
            print(f"Unknown mode: {mode}")
            sys.exit(1)

if __name__ == "__main__":
    main()