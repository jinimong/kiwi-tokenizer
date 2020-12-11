import csv
import sys

from kiwipiepy import Kiwi
from collections import Counter


kiwi = Kiwi()
kiwi.prepare()

valid_token_set = {'NNG', 'NNP', 'NNB'}

def tokenize(text: str):
    result = Counter()
    tokens = kiwi.analyze(text)[0][0]
    return Counter([
        (token[0], token[1])
        for token in tokens
        if token[1] in valid_token_set
    ]).most_common()

def save_tokens_result_to_csv(filename, text, encoding="utf-8"):
    with open(filename, 'w', encoding=encoding, newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['형태소', '품사', 'count'])
        for key, value in tokenize(text):
            writer.writerow([key[0], key[1], value])

        print(filename, '추출 완료.')
