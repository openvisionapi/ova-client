default:
    @just --list

setup:
    #!/usr/bin/env bash
    poetry install --group main

dev:
    #!/usr/bin/env bash
    poetry install

demo:
    #!/usr/bin/env bash
    python3 -m venv .venv &&
    poetry run ./ova.py detection --visualize images/cat.jpeg

update:
    #!/usr/bin/env bash
    poetry update

test:
    #!/usr/bin/env bash
    poetry run pytest tests
