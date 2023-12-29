install:
	poetry install

lint:
	black --config .black.toml . && \
	mypy . && \
	ruff --config .ruff.toml --fix .
