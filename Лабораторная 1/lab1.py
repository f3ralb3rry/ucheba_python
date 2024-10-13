numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
miss_number = numbers.index(None)
len_numbers = len(numbers)
sum_numbers = sum(num for num in numbers if num is not None)
average = sum_numbers / len_numbers
numbers[miss_number] = average
print("Измененный список:", numbers)
