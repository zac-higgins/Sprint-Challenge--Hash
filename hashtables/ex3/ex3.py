def intersection(arrays):
    intersections = {}
    output = []
    for array in arrays:
        for number in array:
            if number in intersections:
                intersections[number] += 1
            else:
                intersections[number] = 1
    for number in intersections:
        # print(intersections[number])
        if intersections[number] == len(arrays):
            output.append(number)
    # output.sort()
    return output




if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
    # print(intersection([
    #         [1,2,3],
    #         [1,4,5],
    #         [1,6,7]
    #     ]))