import os

from tokenizer import save_tokens_result_to_csv


root_path = './target2'


def tree_printer(root):
    for root, dirs, files in os.walk(root):
        for d in dirs:
            print('d', os.path.join(root, d))
        for f in files:
            print('f', os.path.join(root, f))


for root, dirs, files in os.walk(root_path):

    if root_path == root:
        print('Pass', root)
        continue

    text = ''
    print(root, '경로 탐색 중...')

    for f in files:

        filename, ext = os.path.splitext(f)
        if ext != '.txt':
            continue

        with open(os.path.join(root, f), 'r') as f:
            text += f.read()

    save_tokens_result_to_csv(
        ".".join([f"{root}", 'csv']),
        text,
    )