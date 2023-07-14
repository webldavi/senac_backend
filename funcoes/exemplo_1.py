def _sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def _biggest(numbers):
        bigger = numbers[0]
        for number in numbers:
            if number > bigger:
                bigger = number
        return bigger
print(_biggest([1, 2, 3, 4, 5,]))
