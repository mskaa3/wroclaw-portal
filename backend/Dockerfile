FROM python:3.9

WORKDIR /app

EXPOSE 5000

COPY Pipfile Pipfile.lock 

RUN pip install pipenv
# RUN pipenv lock --requirements > requirements.txt
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . ./

CMD ["python","app.py"]