## OpenVisionAPI Client

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

### Demo
```
$ make demo
```

### Want to use httpie ?
```
$ pip install --user httpie
$ http -f POST https://api.openvisionapi.com/api/v1/detection  model="yolov4" image@images/cat.jpeg

HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 128
Content-Type: application/json
Date: Sat, 08 May 2021 18:08:03 GMT
Server: nginx
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload

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
