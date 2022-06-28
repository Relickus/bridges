FROM python:3.10

WORKDIR /bridges
RUN pip install --upgrade pip

COPY pyproject.toml /bridges/
COPY poetry.lock /bridges/

RUN pip install poetry
RUN poetry install

COPY ./ /bridges/

CMD ["poetry","run","python","bridges/main.py"]