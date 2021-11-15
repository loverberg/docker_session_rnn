# docker_session_rnn
# Torch, FastAPI, Docker

NLP: Классификация фамилий с использованием рекуррентных нейронных сетей (RNN)

В этом демонстрационном проекте реализована RNN для классификации слов, обученная на предварительно
обработанных данных для моделирования NLP-моделей “с нуля”, без использования удобных функций,
таких как `torchtext`, с целью формирования представления о препроцессенге для NLP на низком уровне.

Сохраненная модель RNN преобразована в функцию, принимающая запросы, и возвращающая результат прогноза. 
В свою очередь, функция использована для сервера API (бекенда) и размещена в контейнерe Docker на сервере 
под управлением Oracle Linux (Oracle Cloud).

Итоговый контейнер: $ docker pull intercept/rnn_case
