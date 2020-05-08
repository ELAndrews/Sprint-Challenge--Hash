def intersection(arrays):

    """
    YOUR CODE HERE
    """

    result = []

    table = {}

    for arr in arrays:
        for i in arr:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1

    for i, v in enumerate(table):
        if table[v] == len(arrays):
            result.append(v)

    # print(table, result)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))


arrays = [
            list(range(1000000, 2000000)) + [1,2,3],
            list(range(2000000, 3000000)) + [1,2,3],
            list(range(3000000, 4000000)) + [1,2,3],
            list(range(4000000, 5000000)) + [1,2,3],
            list(range(5000000, 6000000)) + [1,2,3],
            list(range(6000000, 7000000)) + [1,2,3],
            list(range(7000000, 8000000)) + [1,2,3],
            list(range(8000000, 9000000)) + [1,2,3],
            list(range(9000000, 10000000)) + [1,2,3],
            list(range(10000000, 11000000)) + [1,2,3]
        ]

print(intersection(arrays))