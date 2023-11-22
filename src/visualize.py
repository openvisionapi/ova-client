import random

from PIL import Image, ImageDraw, ImageFont


def get_prediction_mask(
    image, bounding_boxe, score, label, color, text_offset=10, opacity=96
):
    x1, y1, x2, y2 = bounding_boxe

    mask = Image.new("RGBA", image.size, color + (0,))
    draw = ImageDraw.Draw(mask)

    font = ImageFont.truetype("fonts/Montserrat-Regular.ttf", 20)
    text_bbox = font.getbbox(label)
    text_x = font.getlength(label)
    text_y = text_bbox[2] - text_bbox[0]
    draw.rectangle([(x1, y1 - text_y), (x1 + text_x, y1)], fill=color + (opacity,))
    draw.text((x1, y1 - text_y), text=label, fill="white", font=font)

    draw.rectangle(((x1, y1), (x2, y2)), fill=color + (opacity,))

    return mask


def apply_masks(image, masks):
    for mask in masks:
        image = Image.alpha_composite(image, mask)
    image = image.convert("RGB")
    return image


def visualize_image_predictions(image, predictions):
    img = Image.open(image)
    img = img.convert("RGBA")

    labels = set([prediction["label"] for prediction in predictions])
    colors = {
        label: (random.randint(0, 200), random.randint(0, 200), random.randint(0, 200))
        for label in labels
    }

    masks = []

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

        mask = get_prediction_mask(
            image=img,
            bounding_boxe=bounding_boxe,
            score=score,
            label=label,
            color=color,
        )
        masks.append(mask)

    img = apply_masks(img, masks)

    return img
