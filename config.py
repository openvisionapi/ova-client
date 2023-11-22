import os


class Config:
    OVA_DETECTION_URL = os.getenv(
        "OVA_DETECTION_URL", "https://api.openvisionapi.com/api/v1/detection"
    )

    OVA_OUTPUT_DIR = os.getenv("OVA_OUTPUT_DIR", "output")


config = Config()
