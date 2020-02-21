
build:
	pip install -e .

test:
	pytest tests

docker-run:
	docker run --rm -it --env-file .env generic-python-template

docker-build:
	docker build . -t generic-python-template
