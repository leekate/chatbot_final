import requests
import xmltodict
import json
from konlpy.tag import Komoran
"""
SIGUN_CD	시군코드
SIGUN_NM	시군명
BIZPLC_NM	사업장명
REFINE_ROADNM_ADDR	소재지도로명주소
REFINE_LOTNO_ADDR	소재지지번주소
REFINE_ZIP_CD	소재지우편번호
BSN_STATE_NM	영업상태명
LOCPLC_FACLT_TELNO	소재지시설전화번호
MEDINST_ASORTMT_NM	의료기관종별명
MEDSTAF_CNT	의료인수
HOSPTLRM_CNT	입원실수
SICKBD_CNT	병상수
TREAT_SBJECT_CONT_INFO	진료과목내용정보
REFINE_WGS84_LAT	위도
REFINE_WGS84_LOGT	경도

의도
인사 - 0 
정보제공 - 1
병원전체 정보제공 - 1-1
        진료과목 - 1-2
        주소 - 1-3
        전화번호 - 1-4
        
병원 리스트 제공 - 2 
    지역(시) 병원 리스트 - 2-1
    지역(시) + 지역(동) 병원리스트 - 2-2
    지역(시) + 의료기관종 병원리스트 - 2-3
    지역(시) + 진료과목 병원리스트 - 2-4
    
# 길찾기, 기타등등
"""

def remove_redundancy(list_A) :           # list 중복제거 함수
    set_list = set(list_A)
    remove_list = list(set_list)
    return remove_list


# # 파일경로 지정
# # corpus.txt에 총 학습 data 저장
# test_corpus = open('total_train.txt', 'a',encoding= 'utf-8')
# u_d = open('../train_tools/dict/test_corpus.txt', 'r', encoding= 'utf-8')#

# """
url = "https://openapi.gg.go.kr/GgHosptlM?KEY=337b4bebd30e4d419b85a1ba8c9c26a2&pSize=1000"
url2 = "https://openapi.gg.go.kr/GgHosptlM?KEY=337b4bebd30e4d419b85a1ba8c9c26a2&pIndex=2&pSize=1000"
content = requests.get(url).content
content2 = requests.get(url2).content

dict = xmltodict.parse(content)
dict2 = xmltodict.parse(content2)

jsonString = json.dumps(dict['GgHosptlM']['row'], ensure_ascii=False)   # <GgHosptlM> 태그의 <row> 정보
jsonString2 = json.dumps(dict2['GgHosptlM']['row'], ensure_ascii=False)

jsonObj = json.loads(jsonString)
jsonObj2 = json.loads(jsonString2)

hospital = []; subject = []; location = [];
tel = []; city = []; s_c = []; type = ['요양병원', '치과병원', '한방병원', '종합병원']; treat = []
letter = []
# subject = ['진료','진찰','과목','전문','종목']
# location = ['주소','위치','가는 길','찾아가기','길찾기','네비게이션','지도','어디','어딨','어떻게 가','어딘지','가는길','네비']
# tel = ['전화','번호','전화번호','연락','연락처']
#
for tag in jsonObj :
                hospital.append(tag['BIZPLC_NM'])
                city.append(tag['SIGUN_NM'])

                split_s_c = str(tag['REFINE_LOTNO_ADDR']).split(' ')
                treat_split = str(tag['TREAT_SBJECT_CONT_INFO']).split(', ')
                for i in treat_split:
                    treat.append(i)
                if len(split_s_c) >= 3 :
                    s_c.append(split_s_c[2])



for tag2 in jsonObj2 :
                hospital.append(tag2['BIZPLC_NM'])
                city.append(tag2['SIGUN_NM'])
                split_s_c = str(tag2['REFINE_LOTNO_ADDR']).split(' ')
                treat_split = str(tag2['TREAT_SBJECT_CONT_INFO']).split(', ')
                for i in treat_split:
                    treat.append(i)
                if len(split_s_c) >= 3 :
                    s_c.append(split_s_c[2])

hospital.append('해암요양병원')
city = remove_redundancy(city)
s_c = remove_redundancy(s_c)
treat = remove_redundancy(treat)
#
#
# f = open('new_test.txt', 'r',encoding= 'utf-8')
f = open('total_train.txt', 'r',encoding= 'utf-8')
# f2 = open('test_ner.txt','r',encoding= 'utf-8')
f3 = open('ner_2.txt', 'a',encoding= 'utf-8')

count = 0; line_counter = 0
for item in f :
    count += 1
    # if count > 484269 :
    if item[-2] == '2' or item[-1] == '2':  # 43까지는 의도클래스(0)에 해당.
        line_counter += 1
        letter.append(item[5:-3])   # indexing
#
komoran = Komoran(userdic= '../../utils/user_dic.txt')
for item in letter :
        # print(';' + item)
        f3.write('; ' + item + '\n')
        morphs = komoran.pos(item)  # 형태소 분석기
        index = 0
        fixed =''
        for token in morphs :
            # if token[0] in hospital : # token[0] : 토큰된 단어 token[1] : 토크나이징 된 토큰의 형태소
            #     hos = '<' + token[0] + ':Hospital>'
            #     fixed = item.replace(token[0], hos)
            # elif token[0] in subject :
            #     sub = '<' + token[0] + ':Subject>'
            #     fixed = fixed.replace(token[0], sub)
            # elif token[0] in location :
            #     loc = '<' + token[0] + ':Location>'
            #     fixed = fixed.replace(token[0], loc)
            # elif token[0] in tel :
            #     t = '<' + token[0] + ':Tel>'
            #     fixed = fixed.replace(token[0], t)
        # if fixed == '' : print(item, fixed)
        # else : f3.write('$'+fixed+'\n')
        # for token2 in morphs :
        #     index += 1
        #     if token2[0] in hospital :
                # print('{0}\t{1}\t{2} B_Hospital'.format(index, token2[0], token2[1]))
                # f3.write('{0}\t{1}\t{2} B_Hospital'.format(index, token2[0], token2[1]))
            # elif token2[0] in subject :
            #     # print('{0}\t{1}\t{2} B_Subject'.format(index, token2[0], token2[1]))
            #     f3.write('{0}\t{1}\t{2} B_Subject'.format(index, token2[0], token2[1]))
            # elif token2[0] in location :
            #    # print('{0}\t{1}\t{2} B_Location'.format(index, token2[0], token2[1]))
            #      f3.write('{0}\t{1}\t{2} B_Location'.format(index, token2[0], token2[1]))
            # elif token2[0] in tel :
            #     #print('{0}\t{1}\t{2} B_Tel'.format(index, token2[0], token2[1]))
            #     f3.write('{0}\t{1}\t{2} B_Tel'.format(index, token2[0], token2[1]))
            # else :
        #         print('{0}\t{1}\t{2} O'.format(index, token2[0], token2[1]))
        # print()
        #         f3.write('{0}\t{1}\t{2} O'.format(index, token2[0], token2[1]))
        #     f3.write('\n')
        # f3.write('\n')

            if token[0] in city : # token[0] : 토큰된 단어 token[1] : 토크나이징 된 토큰의 형태소
                hos = '<' + token[0] + ':City>'
                fixed = item.replace(token[0], hos)
            elif token[0] in s_c :
                sc = '<' + token[0] + ':S_c>'
                if token[0] == '정왕동' or token[0] == '신천동' : fixed = item.replace(token[0], sc)
                else : fixed = fixed.replace(token[0], sc)
            elif token[0] in type :
                tp = '<' + token[0] + ':Type>'
                fixed = fixed.replace(token[0], tp)
            elif token[0] in treat :
                tr = '<' + token[0] + ':Treat>'
                fixed = fixed.replace(token[0], tr)
        if fixed == '' : print("에러")
        else : f3.write('$'+fixed+'\n')
        #
        for token2 in morphs :
            index += 1
            if token2[0] in city : # token[0] : 토큰된 단어 token[1] : 토크나이징 된 토큰의 형태소
                f3.write('{0}\t{1}\t{2} B_City'.format(index, token2[0], token2[1]))
            elif token2[0] in s_c :
                f3.write('{0}\t{1}\t{2} B_S_c'.format(index, token2[0], token2[1]))
            elif token2[0] in type :
                f3.write('{0}\t{1}\t{2} B_Type'.format(index, token2[0], token2[1]))
            elif token2[0] in treat :
                f3.write('{0}\t{1}\t{2} B_Treat'.format(index, token2[0], token2[1]))
            else :
                f3.write('{0}\t{1}\t{2} O'.format(index, token2[0], token2[1]))
            f3.write('\n')
        f3.write('\n')
        # print()
print(line_counter)
f.close()
f3.close()













# url2 = "https://openapi.gg.go.kr/ChildNightTreatHosptl?KEY=77cb354acba545899e78bf1bfe9c159c&pSize=1000"
# content2 = requests.get(url2).content
# dict2 = xmltodict.parse(content2)
# jsonString2 = json.dumps(dict2['ChildNightTreatHosptl']['row'], ensure_ascii=False)
# jsonObj2 = json.loads(jsonString2)

