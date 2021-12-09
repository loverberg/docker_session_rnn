# NLP: RNN + API + Docker + Oracle_Cloud

В этом демонстрационном проекте реализована RNN для классификации слов, обученная на предварительно
обработанных данных для моделирования NLP-моделей.

Сохраненная модель RNN преобразована в функцию, принимающая запросы, и возвращающая результат прогноза. 
В свою очередь, функция использована для сервера API (бекенда) и размещена в контейнерe Docker на сервере 
под управлением Oracle Linux (Oracle Cloud).

# Ход работы:

| [Обучение модели](https://github.com/loverberg/docker_session_rnn/blob/main/rnn_classification.ipynb)      |
| [prediction](https://github.com/loverberg/docker_session_rnn/blob/main/prediction.py)      |
| [API](https://github.com/loverberg/docker_session_rnn/blob/main/fast.py)      | 

# Итоговый контейнер: $ docker pull intercept/rnn_case

#Torch #FastAPI #Docker
