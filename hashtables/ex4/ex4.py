def has_negatives(a):
    numbers = {}
    result = []
    for number in a:
        if number > 0:
            if number not in numbers:
                numbers[number] = 1
            else:
                numbers[number] += 1
        if number < 0:
            positive = number * -1
            if positive not in numbers:
                numbers[positive] = 1
            else:
                numbers[positive] += 1
    for number in numbers:
        if numbers[number] > 1:
            result.append(number)

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
