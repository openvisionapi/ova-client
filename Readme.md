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
