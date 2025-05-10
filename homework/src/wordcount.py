# Ejemplo del cado de uso:
# python3 -m homework data/input data/output
import os

from homework.src._internals import (
    count_words,
    parse_args,
    preprocess_lines,
    read_all_lines,
    split_into_words,
    write_word_counts,
)


def main():
    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)
    preprocessed_lines = preprocess_lines(lines)
    words = split_into_words(preprocessed_lines)
    word_counts = count_words(words)
    write_word_counts(output_folder, word_counts)
