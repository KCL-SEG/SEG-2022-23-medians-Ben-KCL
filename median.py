numbers = []

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
length = len(numbers)
if length % 2 == 0:
	median = 0.5 * (numbers[int(length / 2)] + numbers[int(length / 2) + 1])
	print(median)
else:
	print(numbers[(length + 1) / 2])
