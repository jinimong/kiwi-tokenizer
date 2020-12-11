import os

from tokenizer import save_tokens_result_to_csv

def tree_printer(root):
    for root, dirs, files in os.walk(root):
        for d in dirs:
            print('d', os.path.join(root, d))
        for f in files:
            print('f', os.path.join(root, f))

# tree_printer('./target')
# file_txt = './target/1-1-3. 지방분권/중앙정부가 중앙집권적으로 교육을 통제하는 시스템을 근본적으로 개선하자..txt'
# file_pdf = './target/1-1-1. 공통/교육과정상의 중앙집권과 지방분권.pdf'
# target_path = file_pdf

root_path = './target'

for root, dirs, files in os.walk(root_path):

    for f in files:

        filename, ext = os.path.splitext(f)
        if ext != '.txt':
            continue

        output_filename = os.path.join(root, ".".join([filename, 'csv']))
        if os.path.exists(output_filename):
            continue

        with open(os.path.join(root, f), 'r') as f:
            save_tokens_result_to_csv(output_filename, f.read())