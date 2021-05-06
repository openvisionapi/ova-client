import random

from PIL import Image, ImageDraw, ImageFont


def draw_bounding_boxe_on_image(image, bounding_boxe, score, label, color, text_offset=10):
    x1, y1, x2, y2 = bounding_boxe

    draw = ImageDraw.Draw(image)

    draw.rectangle(((x1, y1), (x2, y2)), outline=color, width=3)

    font = ImageFont.load_default()
    text_x, text_y = font.getsize(label)
    draw.rectangle(((x1, y1), (x1 + text_x, y1 - text_y)), fill=color)
    draw.text((x1, y1 - text_y), text=label, fill="white", font=font)


def visualize_image_predictions(image, predictions):
    img = Image.open(image)
    labels = set([prediction["label"] for prediction in predictions])
    colors = {
        label: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for label in labels
    }
    for prediction in predictions:
        bounding_boxe = (
            prediction["bbox"]["x1"],
            prediction["bbox"]["y1"],
            prediction["bbox"]["x2"],
            prediction["bbox"]["y2"],
        )
        score = prediction["score"]
        label = prediction["label"]
        color = colors[label]
        draw_bounding_boxe_on_image(
            image=img, bounding_boxe=bounding_boxe, score=score, label=label, color=color
        )
    return img
