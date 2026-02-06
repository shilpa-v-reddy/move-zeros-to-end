def move_zeros(numbers):
    non_zero = 0

    for index in range(len(numbers)):
        if numbers[index] != 0:
            temp = numbers[non_zero]
            numbers[non_zero] = numbers[index]
            numbers[index] = temp
            non_zero = non_zero + 1
    return numbers
#array = [0,1,0,3,2]
array = [3,6,8,0,0,2,8,0]
move_zeros(array)
print(f"array after the zeros moved to ends:{array}")