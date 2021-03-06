FROM python:3.8.10
WORKDIR /app

EXPOSE 8080

COPY ./fast.py .
COPY ./model_rnn .
COPY ./prediction.py .
COPY ./structure_model.py .
COPY ./requirements.txt .

RUN pip install -r requirements.txt

CMD ["uvicorn", "fast:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]