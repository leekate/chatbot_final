f = open('ner_train.txt', 'r', encoding='utf-8')
f2 = open('intent1_ner.txt', 'a', encoding='utf-8')

# lines = []
# for item in f :
#     if item[0] == ';' :
#         lines.append(item)
#     elif item[0] == '$' :
#         lines.append(item.replace(' 종목', ' <종목:Subject>'))
#     else :
#         lines.append(item.replace('\t종목\tNNG O', '\t종목\tNNG Subject'))
#
# for i in lines :
#     f2.write(i)



