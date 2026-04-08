.PHONY: install brain-games

install:
	uv sync

brain-games:
	uv run brain-games