
build:
	pip install -e .

docker-run:
	docker run --rm -it --env-file .env generic-python-template

docker-build:
	docker build . -t generic-python-template
