<div align="center">
<h1> OpenVisionAPI Client </h1>

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

</div>

## 🚀 Getting Started

### Prerequisites

### Installing
Install the dependencies
```
$ make setup
```

### Usage
```
$ source .venv/bin/activate
$ ./ova_client.py detection /path/to/image
```

The available options for the cli:
```
./ova_client.py detection --help
Usage: ova_client.py detection [OPTIONS] IMAGE

Options:
  -s, --save       Save the output image.
  -v, --visualize  Draw bounding boxes on the detected objects.
  --help           Show this message and exit.
```

### Quick demo
```
$ make demo
```

### Want to use httpie ?
```
$ pip install --user httpie
$ http -f POST https://api.openvisionapi.com/api/v1/detection  model="yolov4" image@images/cat.jpeg

{
    "description": "Detected objects",
    "predictions": [
        {
            "bbox": {
                "x1": 442,
                "x2": 982,
                "y1": 199,
                "y2": 1270
            },
            "label": "cat",
            "score": "0.93"
        }
    ]
}
```

### Want to use curl ?
```
$ curl -X POST https://api.openvisionapi.com/api/v1/detection \
  -F "model=yolov4" \
  -F "image=@images/cat.jpeg"

{
  "description": "Detected objects",
  "predictions": [
    {
      "bbox": {
        "x1": 442,
        "x2": 982,
        "y1": 199,
        "y2": 1270
      },
      "label": "cat",
      "score": "0.93"
    }
  ]
}
```

### Configuration
The configuration can be set up using the following env variables:

**DETECTION_URL** : The URL to the OpenVisionAPI server. The default is `https://api.openvisionapi.com/api/v1/detection`

**DETECTION_MODEL** : The object detection model to use. The default is `yolov4`

**RESULT_DIR** : The directory where to store the result. The default is `./results`


## ⛏️  Built Using
- [Pillow](https://github.com/python-pillow/Pillow)
- [click](https://github.com/pallets/click)
- [requests](https://github.com/psf/requests)
- [pygments](https://github.com/pygments/pygments)

## ✍️  Author
[Badr BADRI](https://github.com/pythops)

## 🤝 Contributing
Your contributions are welcome !

### Setting up development environment
To setup the development environment, simply run this command
```
$ make dev
```
### Code-style checks
[black](https://github.com/psf/black) is used for code formatting.

[mypy](https://github.com/python/mypy) is used for static typing.

## 🔧 Tests
To run the tests, simply run those commands
```
$ make dev
$ make test
```

## ⚖️  License
AGPLv3

Copyright © 2021 Badr BADRI @pythops
