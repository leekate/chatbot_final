from Hospital_INFO_Chatbot.utils.Preprocess import Preprocess
from Hospital_INFO_Chatbot.models.intent.IntentModel import IntentModel

p = Preprocess(word2index_dic='/Users/jiwoo/PycharmProjects/chatbot_final/Hospital_INFO_Chatbot/train_tools/dict/chatbot_dict.bin',
               userdic='/Users/jiwoo/PycharmProjects/chatbot_final/Hospital_INFO_Chatbot/utils/user_dic.txt')

intent = IntentModel(model_name='/Users/jiwoo/PycharmProjects/chatbot_final/Hospital_INFO_Chatbot/models/intent/intent_model.h5', proprocess=p)
query = []

# query.append('하이!')
query.append('주변 피부과 병원')
# query.append('병원 리스트 알려줘')
# query.append('고양시 덕양구 병원 리스트 알려줘')
# query.append('김포시')
# query.append('안양윌스기념병원 정보')
# query.append('남양주시')
# query.append('남양주')

for item in query :
    predict = intent.predict_class(item)
    predict_label = intent.labels[predict]
    print(item)
    print("=======================")
    print("의도 예측 클래스 : ", predict)
    print("의도 예측 레이블 : ", predict_label)
