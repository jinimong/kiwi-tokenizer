import csv
import sys

from kiwipiepy import Kiwi
from collections import Counter


kiwi = Kiwi()
kiwi.prepare()

file_path = 'example.txt'
if len(sys.argv) > 1 and sys.argv[1]:
    file = sys.argv[1] 
file_name, ext = file_path.split('.')

valid_token_set = {'NNG', 'NNP', 'NNB'}

print('=====')

result = Counter()

with open(file_path) as f:
    text = f.read()
    tokens = kiwi.analyze(text)[0][0]
    result = Counter([
        (token[0], token[1])
        for token in tokens
        if token[1] in valid_token_set
    ])

output_path = '.'.join([file_name, 'csv'])
with open(output_path, 'w' ) as f:
    writer = csv.writer(f)
    writer.writerow(['형태소', '품사', 'count'])
    for key, value in result.items():
        writer.writerow([key[0], key[1], value])

    print(file_path, '>>', output_path, '추출 완료.')

print('=====')
