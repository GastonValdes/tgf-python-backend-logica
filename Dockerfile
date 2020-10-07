FROM python:3.8-alpine 

RUN mkdir /logica
WORKDIR /logica
COPY requirements.txt /logica
RUN pip install -r requirements.txt
COPY . /logica
CMD ["python", "./main.py", "--host", "0.0.0.0"]