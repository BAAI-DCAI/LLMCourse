# LLMCourse

# Preparation
#### Create DashScope account and API key

[Tutorial](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key)

#### Prepare DashScope development environment
Python 3.8+:
```Python
pip install dashscope
```
[Tutorial](https://help.aliyun.com/zh/dashscope/developer-reference/install-dashscope-sdk)

#### Clone this repository
```
git clone https://github.com/BAAI-DCAI/LLMCourse.git
```

# Data
We select a sample of 100 images from Visual Genome dataset, an open-source resource that offers comprehensive manual annotations for 108K images.

The images are available in [data/images.zip](data/images.zip), while the annotations are located in [data/input.json](data/input.json).

The structure of [data/input.json](data/input.json) is as follows.

```
key: str, image ID
value: dict, annotations
    width: image width
    height: image height
    captions: list, 5 sentences describing the image
    objects: list, object information
        x: top left coordinate
        y: top left coordinate
        w: bounding box width
        h: bounding box height
        names: list, object name
    regions: list, region information
        x: top left coordinate
        y: top left coordinate
        width: bounding box width
        height: bounding box height
        phrase: str, region description
```

# Exercises

#### Exercise 1
Generate detailed description for images using Qwen-VL, provided with the images.

A sample code snippet can be found in [src/generate_v1.py](src/generate_v1.py).

#### Exercise 2
Generate detailed description for images using Qwen-VL, provided with the images and manual annotations, including captions, objects and regions.

A sample code snippet can be found in [src/generate_v2.py](src/generate_v2.py).

#### Exercise 3
Generate detailed description for images using Qwen-turbo, provided with the manual annotations, including captions, objects and regions.

A sample code snippet can be found in [src/generate_v3.py](src/generate_v3.py).
