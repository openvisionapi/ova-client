import filecmp
from unittest.mock import patch

import responses  # type: ignore
from click.testing import CliRunner

from config import config
from ova import cli


@responses.activate
def test_detection_cli_with_visualize_option(tmpdir, monkeypatch):
    detection_response = {
        "description": "Detected objects",
        "predictions": [
            {
                "bbox": {"x1": 442, "x2": 982, "y1": 199, "y2": 1270},
                "label": "cat",
                "score": "0.93",
            }
        ],
    }
    responses.add(responses.POST, config.DETECTION_URL, json=detection_response)

    monkeypatch.setattr(config, "RESULT_DIR", str(tmpdir))

    with patch("random.randint", return_value=0):
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "detection",
                "testdata/detection/input_image.jpeg",
                "--visualize",
                "--save",
            ],
        )

    assert result.exit_code == 0
    assert filecmp.cmp(
        "testdata/detection/expected_image.jpeg", f"{str(tmpdir)}/input_image.jpeg"
    )


@responses.activate
def test_detection_cli_without_visualize_option():
    detection_response = {
        "description": "Detected objects",
        "predictions": [
            {
                "bbox": {"x1": 442, "x2": 982, "y1": 199, "y2": 1270},
                "label": "cat",
                "score": "0.93",
            }
        ],
    }
    responses.add(responses.POST, config.DETECTION_URL, json=detection_response)

    runner = CliRunner()
    result = runner.invoke(cli, ["detection", "testdata/detection/input_image.jpeg"])

    assert result.exit_code == 0
