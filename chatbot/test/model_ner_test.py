import sys
sys.path.append('.')
from chatbot.utils.Preprocess import Preprocess
from chatbot.models.ner.NerModel import NerModel

p = Preprocess(word2index_dic='chatbot/train_tools/dict/chatbot_dict.bin',
               userdic = 'chatbot/utils/user_dic.tsv')


ner = NerModel(model_name='chatbot/models/ner/ner_model.h5', proprocess=p)
query = '오늘 오전 13시 2분에 탕수육 주문 하고 싶어요'
predicts = ner.predict(query)
tags = ner.predict_tags(query)
print(predicts)
print(tags)

