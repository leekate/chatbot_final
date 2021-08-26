## 프로젝트 구조

* chatbot
    * train_tools
    * models
        * intent
        * ner
    * utils
    * config
    * test

[train_tools](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/train_tools) : 챗봇 학습툴 관련 파일
[models](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/models) : 챗봇 엔진에서 사용하는 딥러닝 모델 관련 파일
**intent** : 의도 분류 모델 관련 파일
**ner** : 개체 인식 모델 관련 파일
[utils](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/utils) : 챗봇 개발에 필요한 유틸리티 라이브러리
[config](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/config) : 챗봇 개발에 필요한 전역설정
[test](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/test) : 챗봇 개발에 필요한 테스트 코드

## 엔진 처리 과정
* 전처리 과정
    * 전처리
    * 단어 사전 구축 및 시퀀스 생성
* 의도 분석
* 개체명 인식
* 답변 검색
    * 데이터베이스 제어모듈 생성
* 답변 출력
    * 답변 검색 모듈 생성

## 엔진 서버 개발






