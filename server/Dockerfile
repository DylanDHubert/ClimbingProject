FROM python:alpine

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

COPY requirements.txt requirments.txt
RUN pip install -r requirments.txt

EXPOSE 5000


CMD ["python", "app.py"]