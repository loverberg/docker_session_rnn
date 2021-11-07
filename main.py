# Импортируем Flask для создания API
from flask import Flask, request

# Импортируем prediction
from prediction import *

app = Flask(__name__)

# СоздаЁм конечную точку API
@app.route('/predict')
def api_predict():
   # Считываем параметры запроса
   fename = request.args.get('fename')

# Используем метод модели predict
# Возвращаем результат
   req = predict(fename)
   return fename + ': ' + str(req[0][1])
if __name__ == '__main__':
   app.run()