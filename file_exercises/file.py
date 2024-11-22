def print_number_of_word(file_name: str, chosen_word: str):
    with open(file_name) as file:
        words = file.read().split()
        print(len(list(filter(lambda word: word.__contains__(chosen_word), words))))


def get_dict_words(file_name: str) -> dict[str, int]:
    with open(file_name) as file:
        words: list[str] = file.read().split()
        result: dict[str, int] = {}
        for word in words:
            word = word.upper().split(",")[0]
            word = word.split(".")[0]
            if result.get(word):
                result[word] += 1
            else:
                result[word] = 1
        return result


def get_filtered_words(file_name: str) -> list[tuple[str, int]]:
    dictionary = get_dict_words(file_name)
    dictionary = list(filter(lambda pair: pair[1] > 1, dictionary.items()))
    return dictionary
