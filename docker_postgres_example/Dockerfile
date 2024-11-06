FROM python:latest

RUN mkdir -p /home/project
COPY . /home/project
RUN pip install psycopg2 pandas matplotlib sqlalchemy
CMD ["python", "/home/project/main.py"]
