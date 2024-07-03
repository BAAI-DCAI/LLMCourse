import dashscope
import glob
import json
import time
from http import HTTPStatus
from dashscope import MultiModalConversation

# TBD
image_dir = 'images'
prompt_file = 'prompt_v1.txt'
output_file = f'output_v1.json'
sample_num = 1
dashscope.api_key = ''
    
def call_with_local_file(input_text, image_path):
    # TBD
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