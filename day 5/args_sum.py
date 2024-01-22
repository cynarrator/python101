def sum(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    print(sum)

sum(1, 2, 3, 4, 5)