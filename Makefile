SHELL := /bin/bash

setup:
	@(\
	    python3 -m venv .venv && \
	    source .venv/bin/activate &&  \
	    pip3 install -U pip && \
	    pip3 install -r requirements/common.txt \
	)

demo:
	@(\
	    source .venv/bin/activate && \
	    ./ova_client.py detection --visualize images/cat.jpeg \
	)

test:
	@(\
	    source .venv/bin/activate && \
	    flake8 && \
	    pytest \
	)

dev:
	@(\
	    python3 -m venv .venv && \
	    source .venv/bin/activate &&  \
	    pip3 install -U pip && \
	    pip3 install -r requirements/common.txt && \
	    pip3 install -r requirements/dev.txt \
	)

pip-update:
	@(\
	    source .venv/bin/activate &&  \
	    pip-compile --output-file=requirements/common.txt requirements/common.in && \
	    pip-compile --output-file=requirements/dev.txt requirements/dev.in \
	)
