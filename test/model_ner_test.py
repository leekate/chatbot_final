from utils.Preprocess import Preprocess
from models.ner.NerModel import NerModel

p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
               userdic='../utils/user_dic.txt')

ner = NerModel(model_name='../models/ner/ner_train.h5', proprocess=p)
query = '김포시 한방병원 리스트 알려주라'
predicts = ner.predict(query)
tags = ner.predict_tags(query)
print(predicts)
print(tags)