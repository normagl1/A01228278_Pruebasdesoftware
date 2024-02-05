import sys
import time

def read_numbers_from_file(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Invalid data '{line.strip()}' encountered and will be skipped.")
    return numbers

def calculate_mean(numbers):
    total_sum = sum(numbers)
    count = len(numbers)
    return total_sum / count

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def calculate_mode(numbers):
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_frequency = max(frequency.values())
    modes = [key for key, val in frequency.items() if val == max_frequency]
    return modes[0] if len(modes) == 1 else modes

def calculate_variance(numbers, mean):
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_std_dev(variance):
    return variance ** 0.5

def execute_function(function_name, numbers):
    if function_name == 'mean':
        result = calculate_mean(numbers)
    elif function_name == 'median':
        result = calculate_median(numbers)
    elif function_name == 'mode':
        result = calculate_mode(numbers)
    elif function_name == 'variance':
        mean = calculate_mean(numbers)
        result = calculate_variance(numbers, mean)
    elif function_name == 'std_dev':
        mean = calculate_mean(numbers)
        variance = calculate_variance(numbers, mean)
        result = calculate_std_dev(variance)
    else:
        print(f"Function {function_name} is not recognized.")
        sys.exit(1)
    return result

def main():
    start_time = time.time()
    if len(sys.argv) < 3:
        print("Usage: python computeStatistics.py <function_name> fileWithData.txt")
        sys.exit(1)

    function_name = sys.argv[1]
    file_path = sys.argv[2]
    numbers = read_numbers_from_file(file_path)

    if not numbers:
        print("No valid data found.")
        sys.exit(1)

    result = execute_function(function_name, numbers)
    print(f"{function_name.capitalize()}: {result}")

    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time} seconds")

if __name__ == "__main__":
    main()