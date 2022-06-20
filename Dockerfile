FROM python:3.11-rc-buster

COPY . /app/src

EXPOSE 8000:8000

WORKDIR /app/src

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]