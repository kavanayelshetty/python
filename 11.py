numbers = [12, 45, 7, 89, 23, 89, 56]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second largest number:", unique_numbers[-2])
else:
    print("No second largest number exists.")