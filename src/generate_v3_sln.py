import dashscope
import json
import time
from http import HTTPStatus

image_dir = 'images'
input_file = 'input.json'
prompt_file = 'prompt_v3.txt'
output_file = f'output_v3.json'
sample_num = 1
dashscope.api_key = ''

def get_bbox_string(x, y, w, h, image_width, image_height):
    # normalize bounding box to [0, 1]
    top_left_x = min(1, max(0, round(x / image_width, 3)))
    top_left_y = min(1, max(0, round(y / image_height, 3)))
    bottom_right_x = min(1, max(0, round((x + w) / image_width, 3)))
    bottom_right_y = min(1, max(0, round((y + h) / image_height, 3)))
            
    return '[' + str(top_left_x) + ', ' + str(top_left_y) + ', ' \
            + str(bottom_right_x) + ', ' + str(bottom_right_y) + ']'

def get_rd_with_bbox(record):
    rds = list()
    for r in record['regions']:
        bbox_string = get_bbox_string(r['x'], r['y'], r['width'], r['height'], record['width'], record['height'])
        rd = r['phrase'].strip() + ': ' + bbox_string
        rds.append(rd)
        
    return '\n'.join(rds)

def get_od_with_bbox(record):
    ods = list()
    for o in record['objects']:
        bbox_string = get_bbox_string(o['x'], o['y'], o['w'], o['h'], record['width'], record['height'])
        # there might be more than one object names and we only pick the first one
        od = o['names'][0].strip() + ': ' + bbox_string
        ods.append(od)

    return '\n'.join(ods)

def get_caption(record):
    return '\n'.join(record['captions'])
    
def call_with_messages(input_text):
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': input_text}]

    response = dashscope.Generation.call(
        dashscope.Generation.Models.qwen_turbo,
        messages=messages,
        result_format='message',
    )
    
    if response.status_code == HTTPStatus.OK:
        return response['output']['choices'][0]['message']['content']
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
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