FROM python:3.10.11

WORKDIR /

RUN pip install pipenv

COPY Pipfile* ./

RUN pipenv install --system

RUN pipenv sync

COPY . .

EXPOSE 3002

CMD [ "pipenv", "run", "python", "main.py", "develop"]