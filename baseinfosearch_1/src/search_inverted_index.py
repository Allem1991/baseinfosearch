from collections import defaultdict
from typing import Tuple, List


def read_inverted_index_file() -> dict:
    result = defaultdict(set)
    with open("inverted_index.txt") as f:
        for line in f:
            data = line.split(" ")
            word = data.pop(0)
            documents = data
            result[word] = set(documents)

    return result


inverted_index = read_inverted_index_file()
to_search = input("Введите запрос AND, OR, NOT: ")


def process_search(search_request: str) -> Tuple[List[str], List[str]]:
    BOOL_OPERANDS = {"AND", "OR", "NOT"}
    splited = search_request.split(" ")
    bool_operands_in_request = []
    search_request_array = []
    for word in splited:
        if word in BOOL_OPERANDS:
            bool_operands_in_request.append(word)
        else:
            search_request_array.append(word)

    return search_request_array, bool_operands_in_request


search_request_array, bool_operands_in_request = process_search(to_search)

result = inverted_index[search_request_array[0]]


for i in range(1, len(search_request_array)):
    word = search_request_array[i]
    operand = bool_operands_in_request[i - 1]

    if operand == "OR":
        result = result | inverted_index[word]
    elif operand == "AND":
        result = result & inverted_index[word]
    else:
        result = result - inverted_index[word]

print('.html '.join(result))
