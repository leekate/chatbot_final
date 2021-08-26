## 프로젝트 구조

* chatbot
    * train_tools
    * models
        * intent
        * ner
    * utils
    * config
    * test

[train_tools](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/train_tools) : 챗봇 학습툴 관련 파일<br/>
[models](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/models) : 챗봇 엔진에서 사용하는 딥러닝 모델 관련 파일<br/>
**intent** : 의도 분류 모델 관련 파일<br/>
**ner** : 개체 인식 모델 관련 파일<br/>
[utils](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/utils) : 챗봇 개발에 필요한 유틸리티 라이브러리<br/>
[config](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/config) : 챗봇 개발에 필요한 전역설정<br/>
[test](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/test) : 챗봇 개발에 필요한 테스트 코드<br/>

## 엔진 처리 과정
* 전처리
    * [전처리 모듈](https://github.com/tmvld97/Hospital_INFO_Chatbot/blob/master/utils/Preprocess.py)
    * [단어 사전 구축 및 시퀀스 생성](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/train_tools/dict)
* [의도파악](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/models/intent)
* [개체명 인식](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/models/ner)
* 답변 검색 및 출력
    * [데이터베이스 제어모듈 생성](https://github.com/tmvld97/Hospital_INFO_Chatbot/blob/master/utils/Database.py)
    * [답변 검색 모듈 생성](https://github.com/tmvld97/Hospital_INFO_Chatbot/blob/master/utils/FindAnswer.py)

## 엔진 서버 개발






