FROM python:3.7


COPY setup.py ./
COPY README.md ./

RUN pip install -e .

COPY . ./

ENTRYPOINT ["myapp"]
