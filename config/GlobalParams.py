# 단어 시퀀스 벡터 크기
MAX_SEQ_LEN = 14
HOS_TYPE = ['요양병원', '한방병원', '종합병원', '치과병원']
HOS_SUBJECT = ['진료', '진찰', '전문', '종목', '진료과목', '진찰과목', '전문과목']
HOS_LOC = ['주소','위치','가는 길','찾아가기','길찾기','네비게이션','지도','어디','어딨','어떻게 가','어딘지','가는길','네비']
HOS_TEL = ['전화','번호','전화번호','연락','연락처']
def GlobalParams():
    global MAX_SEQ_LEN, HOS_TYPE, HOS_SUBJECT, HOS_LOC, HOS_TEL
