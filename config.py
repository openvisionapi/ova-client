import os


class Config:
    DETECTION_URL = os.getenv("DETECTION_URL", "https://api.openvisionapi.com/api/v1/detection")
    DETECTION_MODEL = os.getenv("DETECTION_MODEL", "yolov4")

    RESULT_DIR = os.getenv("RESULT_DIR", "results")


config = Config()
