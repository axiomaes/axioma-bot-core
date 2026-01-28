.PHONY: run test format build

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest tests/

format:
	black app tests
	isort app tests

build:
	docker build -t axioma-bot-core .
