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

[Test.py](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/test)
## 엔진 서버 개발
* Cloud Server
* [TCP socet Server](https://github.com/tmvld97/Hospital_INFO_Chatbot/blob/master/utils/BotServer.py)
* [chatbot main engine server](https://github.com/tmvld97/Hospital_INFO_Chatbot/blob/master/bot.py)
[챗봇 내부 엔진 서버 테스트](https://github.com/tmvld97/Hospital_INFO_Chatbot/blob/master/test/chatbot_client_test.py)<br/>
**테스트 전 메인 엔진 서버 프로그램이 구동된 상태여야 함**

## CHATBOT API
[API 서버 디렉터리](https://github.com/tmvld97/Hospital_INFO_Chatbot/tree/master/chatbot_api)
* chatbot_api
    * app.py
    * KakaoTemplate.py

## 개발노트
1. readme 정리<br/>
2. 동시접속 가능한지 확인 (kakao 09:00~18:00 제한)<br/>
3. 말풍선 i open builder 참고<br/>
4. 추가기능(지역별 경고, 상위4개 진료)<br/>
5. **학습모듈 에러 검출**<br/>
6. **AWS 설정**
