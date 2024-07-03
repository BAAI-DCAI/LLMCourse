import dashscope
import json
import time
from http import HTTPStatus

# TBD
image_dir = 'images'
input_file = 'input.json'
prompt_file = 'prompt_v3.txt'
output_file = f'output_v3.json'
sample_num = 1
dashscope.api_key = ''

def get_bbox_string(x, y, w, h, image_width, image_height):
    # normalize bounding box to [0, 1]
    # TBD
    return ''

def get_rd_with_bbox(record):
    # TBD
    return ''

def get_od_with_bbox(record):
    # TBD
    return ''

def get_caption(record):
    # TBD
    return ''
    
def call_with_messages(input_text):
    # TBD
    return ''


if __name__ == '__main__':
    with open(prompt_file, 'r', encoding='utf8') as fin:
        prompt = fin.read()

    with open(input_file, 'r', encoding='utf8') as fin:
        data = json.load(fin)

    output = dict()
    for id, record in data.items():
        print(id)
        input = f'1. Captions:\n{get_caption(record)}\n\n'
        input += f'2. Objects:\n{get_od_with_bbox(record)}\n\n'
        input += f'3. Regions:\n{get_rd_with_bbox(record)}'
        input_text = f'{prompt}\n{input}'
        result = call_with_messages(input_text)
        output[id] = {'input': input_text, 'output': result}
        #time.sleep(10)

        if len(output) >= sample_num:
            break

    with open(output_file, 'w+', encoding='utf8') as fout:
        fout.write(json.dumps(output, indent=4, ensure_ascii=False))