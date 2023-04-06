FROM python:3.10

WORKDIR /our_Bot_poetry

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "inerf.py"]
