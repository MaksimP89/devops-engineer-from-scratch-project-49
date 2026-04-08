.PHONY: install brain-games build package-install

install:
	uv sync

brain-games:
	uv run brain-games
brain-even:
	uv run brain-even
brain-calc:
	uv run brain-calc
brain-gcd:	
	uv run brain-gcd
build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

fix:
	uv run ruff check --fix .