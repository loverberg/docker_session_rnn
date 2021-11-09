FROM python:3.8.10
WORKDIR /app

EXPOSE 5000

COPY ./main.py .
COPY ./model_rnn .
COPY ./prediction.py .
COPY ./structure_model.py .
COPY ./requirements.txt .

RUN pip install -r requirements.txt

CMD ['python3', './main.py']