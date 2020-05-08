# def finder(files, queries):
#     result = []
#     query_dict = {}
#     for file_path in files:
#         last_part = file_path.rsplit('/', 1)[1]
#         query_dict[last_part] = file_path
#     for query in queries:
#         if query in query_dict:
#             result.append(query_dict[query])

#     return result

def finder(files, queries):
    result = []
    query_dict = {}
    for query in queries:
        query_dict[query] = 0
    for file_path in files:
        last_part = file_path.rsplit('/', 1)[1]
        if last_part in query_dict:
            result.append(file_path)

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
