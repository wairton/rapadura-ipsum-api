import csv
import random


def load_lorem_sentences():
    with open('lorem.txt') as fh:
        return [l.strip() for l in fh.readlines()]


def load_dictionary():
    with open('dictionary.csv') as csv_file:
        return [l for l in csv.DictReader(csv_file, delimiter=',')]


SUFFIXES = ['at', 'it', 'is', 'us', 'et', 'um']
LOREM_SENTENCES = load_lorem_sentences()
EXPRESSIONS = load_dictionary()


def get_expression():
    expression = random.choice(EXPRESSIONS)
    foo = expression['stem'] if len(expression['stem']) > 0 else expression['expression']
    if len(expression['alternatives']) > 0:
        suffix = random.choice(expression['alternatives'].split())
    else:
        suffix = random.choice(SUFFIXES)
    return foo + suffix


def get_sentence():
    sentence = random.choice(LOREM_SENTENCES).split()
    n = len(sentence) // 5  + 1
    expressions = [get_expression() for _ in range(n)]
    for i, expr in zip(random.sample(range(len(sentence)), n), expressions):
        sentence[i] = expr
    return ' '.join(sentence).strip(' .').capitalize() + '.'


if __name__ == '__main__':
    print(get_sentence())
