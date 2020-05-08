def intersection(arrays):

    """
    YOUR CODE HERE
    """

    result = []

    table = {}

    for i in range(len(arrays[0])):
        table[arrays[0][i]] = 0
        i += 1
    
    for arr in arrays:
        for i in arr:
            if i in table.keys():
                table[i] += 1

    for i, v in enumerate(table):
        if table[v] == len(arrays):
            result.append(v)

    return result


# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000,2000000)) + [1,2,3])
#     arrays.append(list(range(2000000,3000000)) + [1,2,3])
#     arrays.append(list(range(3000000,4000000)) + [1,2,3])

#     print(intersection(arrays))




arrays = [ [1,2,3],
            [1,4,5,3],
            [1,6,7,3] ]

# arrays = [
#             list(range(1000000, 2000000)) + [1,2,3],
#             list(range(7000000, 8000000)) + [1,2,3],
#             list(range(8000000, 9000000)) + [1,2,3],
#             list(range(9000000, 10000000)) + [1,2,3],
#             list(range(10000000, 11000000)) + [1,2,3]
#         ]

print(intersection(arrays))