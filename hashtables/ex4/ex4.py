def has_negatives(a):

    """
    YOUR CODE HERE
    """

    table = {}

    result = []

    for i in a:
        if abs(i) in table and abs(i) not in result:
            result.append(abs(i))
        table[abs(i)] = abs(i)
        i += 1

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
