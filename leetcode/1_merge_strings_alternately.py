def my_solution(word1: str, word2: str):
    if len(word1) > len(word2):
        max_len = len(word1)
        min_len = len(word2)
        max_str = word1
    else:
        max_len = len(word2)
        min_len = len(word1)
        max_str = word2

    result = ""
    for index in range(0, max_len):
        if index >= min_len:
            result = result + max_str[index:]
            break
        else:
            result = result + word1[index] + word2[index]

    return result


def best_solution():
    # zip 사용
    pass


word1 = "ab"
word2 = "pqrs"

print(my_solution(word1, word2))