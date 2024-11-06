FROM python:latest

RUN mkdir -p /home/project
COPY . /home/project
RUN pip install pandas matplotlib

WORKDIR /home/project

CMD ["python","/home/project/main.py"]
