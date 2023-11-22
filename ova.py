#!/usr/bin/env python3

import json
from pathlib import Path

import click
import requests
from pygments import formatters, highlight, lexers

from config import config
from src.validators import validate_image
from src.visualize import visualize_image_predictions


@click.group()
def cli():
    pass


@cli.command()
@click.option("-s", "--save", flag_value=True, help="Save the output image.")
@click.option(
    "-v",
    "--visualize",
    flag_value=True,
    help="Draw bounding boxes on the detected objects.",
)
@click.argument("image", type=click.Path(exists=True))
def detection(image, save, visualize):
    mimetype = validate_image(image)

    url = config.DETECTION_URL
    files = {"image": (image, open(image, "rb"), mimetype)}
    body = {"model": config.DETECTION_MODEL}

    try:
        response = requests.post(url=url, files=files, data=body)
        response.raise_for_status()
    except Exception as e:
        raise SystemExit(e)

    predictions = response.json()["predictions"]

    if not visualize:
        output = json.dumps(predictions, indent=4, sort_keys=True)
        print(highlight(output, lexers.JsonLexer(), formatters.TerminalFormatter()))
        return

    img = visualize_image_predictions(image, predictions)

    if save:
        result_dir = config.RESULT_DIR
        Path(result_dir).mkdir(parents=True, exist_ok=True)
        path = Path(f"{result_dir}/{Path(image).name}")
        img.save(path)
    else:
        img.show()


if __name__ == "__main__":
    cli()
