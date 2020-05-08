def finder(files, queries):

    """
    YOUR CODE HERE
    """

    result = []

    table = {}

    for file in files:
        ending = file.split("/")
        table[file] = ending[-1]

    for query in queries:
        for key, value in table.items():
            if value == query:
                result.append(key)

    print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
