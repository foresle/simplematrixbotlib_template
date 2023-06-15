FROM python:3.10-slim

WORKDIR ./code

COPY ./requirements.txt .

RUN pip install python-olm --extra-index-url https://gitlab.matrix.org/api/v4/projects/27/packages/pypi/simple
RUN pip install -r requirements.txt

COPY . .