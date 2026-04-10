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
brain-prime:
	uv run brain-prime	

brain-progression:
	uv run brain-progression
all-brain-games:
	uv run all-brain-games

build:
	uv build

install-brain-games:
	uv tool install dist/*.whl
unnstall-brain-games
	uv tool uninstall hexlet-code

lint:
	uv run ruff check brain_games

fix:
	uv run ruff check --fix .