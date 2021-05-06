import sys

from PIL import Image


def validate_image(image):
    try:
        with Image.open(image) as img:
            return f"image/{img.format.lower()}"
    except Exception as e:
        sys.exit(f"Error: {e.args[0]}")
