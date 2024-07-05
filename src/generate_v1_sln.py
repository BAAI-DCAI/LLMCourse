import dashscope
import glob
import json
import time
from http import HTTPStatus
from dashscope import MultiModalConversation

image_dir = 'images'
prompt_file = 'prompt_v1.txt'
output_file = f'output_v1.json'
sample_num = 1
dashscope.api_key = ''
    
def call_with_local_file(input_text, image_path):
    messages = [{'role': 'user', 'content': [{'image': image_path}, {'text': input_text}]}]
    response = MultiModalConversation.call(
        model='qwen-vl-plus',
        messages=messages
    )
    
    if response.status_code == HTTPStatus.OK:
        return response['output']['choices'][0]['message']['content'][0]['text']
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
        return ''


if __name__ == '__main__':
    with open(prompt_file, 'r', encoding='utf8') as fin:
        prompt = fin.read()

    output = dict()
    image_paths = sorted(glob.glob(f'{image_dir}/*.jpg'))
    
    for image_path in image_paths:
        id = image_path.split('.')[0].split('/')[1]
        print(id)
        result = call_with_local_file(prompt, image_path)
        output[id] = {'input': prompt, 'output': result}
        #time.sleep(10)

        if len(output) >= sample_num:
            break

    with open(output_file, 'w+', encoding='utf8') as fout:
        fout.write(json.dumps(output, indent=4, ensure_ascii=False))