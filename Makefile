PROJ_DIR = bics_nornir

.PHONY: all
all: setup_env tests

.PHONY: setup_env
setup_env:
	curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python && \
		$$HOME/.poetry/bin/poetry config settings.virtualenvs.create false
	$$HOME/.poetry/bin/poetry install	
	
.PHONY: tests
tests:
	-black --check $(PROJ_DIR)
