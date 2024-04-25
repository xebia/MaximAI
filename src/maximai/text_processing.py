import inflect


def transform_numbers_to_text(input_string):
    p = inflect.engine()
    words = input_string.split()
    transformed_words = []
    for word in words:
        if word.isdigit():
            transformed_word = p.number_to_words(word)
            transformed_words.append(transformed_word)
        else:
            transformed_words.append(word)
    return ' '.join(transformed_words)


if __name__ == "__main__":
    input_string = "There are 5 apples and 101 oranges"
    transformed_string = transform_numbers_to_text(input_string)
    print(transformed_string)
