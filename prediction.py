# Импортируем все пакеты, которые необходимы для модели
from structure_model import *
from translate import Translator

def lineToTensor(line):
   tensor = torch.zeros(len(line), 1, n_letters)
   for li, letter in enumerate(line):
      tensor[li][0][letterToIndex(letter)] = 1
   return tensor


def letterToIndex(letter):
   return all_letters.find(letter)


def letterToTensor(letter):
   tensor = torch.zeros(1, n_letters)
   tensor[0][letterToIndex(letter)] = 1
   return tensor


translator = Translator(from_lang="russian",to_lang="english")

def evaluate(line_tensor):
   hidden = rnn.initHidden()

   for i in range(line_tensor.size()[0]):
      output, hidden = rnn(line_tensor[i], hidden)

   return output


def predict(input_line, n_predictions=1):
    input_line = translator.translate(input_line)
    output = evaluate(lineToTensor(input_line))

    # Get top N categories
    topv, topi = output.data.topk(n_predictions, 1, True)
    predictions = []

    for i in range(n_predictions):
        value = topv[0][i]
        category_index = topi[0][i]
        print('(%.2f) %s' % (value, all_categories[category_index]))
        predictions.append([value, all_categories[category_index]])

    return predictions
