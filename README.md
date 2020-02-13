# generic-python-template

A generic python template for small projects.


## Setup local development environment

```bash
git git@github.com:donedeal-giorgio/generic-python-template.git
cd generic-python-template
python3 -m venv .venv
source ./venv/bin/activate
cp .example.env .env
pip install -e .
```

Run the app with:

```bash
myapp
```

## Docker

```
make build
makd run
```
