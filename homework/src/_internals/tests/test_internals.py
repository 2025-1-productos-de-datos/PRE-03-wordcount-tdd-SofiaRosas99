import os
import shutil
import subprocess
import sys

from homework.src._internals.count_words import count_words
from homework.src._internals.parse_args import parse_args
from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.split_into_words import split_into_words


def test_parse_args():

    # Llamada en el prompt:
    #
    #   $ python3 -m homework data/input/ data/output/
    #
    test_args = ["homework", "data/input/", "data/output/"]
    sys.argv = test_args

    input_folder, output_folder = parse_args()

    assert input_folder == test_args[1]
    assert output_folder == test_args[2]


def test_read_all_lines():
    input_folder = "data/input/"
    lines = read_all_lines(input_folder)
    assert len(lines) > 0
    assert any(
        "Analytics refers to the systematic computational analysis of data" in line
        for line in lines
    )


def test_preprocess_lines():
    lines = ["  Hello, World!  ", "Python is GREAT."]
    preprocessed = preprocess_lines(lines)
    assert preprocessed == ["hello, world!", "python is great."]


def test_split_into_words():
    lines = ["hello, world!", "python is great."]
    words = split_into_words(lines)
    assert words == ["hello", "world", "python", "is", "great"]


def test_count_words():
    words = ["hello", "world", "hello", "python"]
    word_counts = count_words(words)
    assert word_counts == {"hello": 2, "world": 1, "python": 1}
