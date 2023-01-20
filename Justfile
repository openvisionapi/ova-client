default:
    @just --list

setup:
    #!/usr/bin/env bash
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip3 install -U pip &&
    pip3 install -r requirements/common.txt

dev:
    #!/usr/bin/env bash
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip3 install -U pip &&
    pip3 install -r requirements/common.txt &&
    pip3 install -r requirements/dev.txt

demo:
    #!/usr/bin/env bash
    python3 -m venv .venv &&
    ./ova_client.py detection --visualize images/cat.jpeg

pip-update:
    #!/usr/bin/env bash
    pip-compile --output-file=requirements/common.txt -U requirements/common.in --resolver=backtracking &&
    pip-compile --output-file=requirements/dev.txt -U requirements/dev.in --resolver=backtracking

test:
    #!/usr/bin/env bash
    source .venv/bin/activate &&
    flake8 &&
    pytest tests
