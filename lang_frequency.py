import argparse
from collections import Counter
import re


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def get_words_from_text(text):
    text_without_digits = re.sub(r'\d+', '', text)
    words_without_punctuation = re.findall(r'\w+', text_without_digits)
    return words_without_punctuation


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    args = parser.parse_args()
    return args


def get_most_frequent_words(words):
    counted_words = Counter(words)
    amount = 10
    return counted_words.most_common(amount)


if __name__ == '__main__':
    try:
        filepath = create_parser().filepath
        text = load_data(filepath)
        words = get_words_from_text(text)
        counted_words = get_most_frequent_words(words)
        print('Самые популярные слова в тексте:')
        for word, count in counted_words:
            print(f'{word} - {count} шт.')
    except FileNotFoundError:
        print('Такого файла не существует')
    except UnicodeDecodeError:
        print('Это не текстовый файл')
