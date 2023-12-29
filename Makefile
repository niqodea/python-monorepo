install:
	poetry install

lint:
	black --config .black.toml . && \
	mypy --config-file .mypy.ini . && \
	ruff --config .ruff.toml --fix .

test:
	pytest .
