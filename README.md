# generic-python-template

A generic python template for small projects.

Useful for python 101 tutorials.

## Setup local development environment

```bash
git git@github.com:donedeal-giorgio/generic-python-template.git
cd generic-python-template
python3 -m venv .venv
source ./venv/bin/activate
cp .example.env .env
pip install -e .
```

## Running the app
Run the app with:

```bash
myapp
```

## Testing

Run tests with
```bash
make tests
```
or 
```bash
pytest tests
```

## Docker

```
make docker-build
makd docker-run
```
