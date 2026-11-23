# Function 1: Calculate the sum
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Function 2: Calculate the mean (average)
def calculate_mean(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


# Function 3: Calculate the median and mode
def calculate_median_mode(numbers):
    sorted_numbers = sorted(numbers)

    # Calculate median
    n = len(sorted_numbers)
    if n % 2 == 1:
        med = sorted_numbers[n // 2]
    else:
        med = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

    # Calculate mode
    mode_num = sorted_numbers[0]
    highest_count = 0

    for num in sorted_numbers:
        count = sorted_numbers.count(num)
        if count > highest_count:
            highest_count = count
            mode_num = num

    return med, mode_num


# Example list
numbers = [2, 4, 4, 6, 8]

# Display results
print("Sum:", calculate_sum(numbers))
print("Mean:", calculate_mean(numbers))

med, mod = calculate_median_mode(numbers)
print("Median:", med)
print("Mode:", mod)