import openpyxl
import pandas as pd
xlsx = pd.read_excel('train_excel.xlsx')
xlsx.to_csv('total_train.csv', index=False)

# f = open('total_train.txt', 'r',encoding= 'utf-8')
# f2 = open('trans.txt', 'r',encoding= 'utf-8')

#
# for i in f :
#     a = i.replace("0000","")
#     b = a.replace("\t\t",",")
#     c = b.replace("\t","")
#     f2.write(c.replace("\n","")+'\n')


# f = open('trans.txt', 'r',encoding= 'utf-8')
# list = f.readlines()
# f.close()
# # #
# file = openpyxl.load_workbook("train_excel.xlsx")
# sheet = file.active
# # #
# def ex() :
#     for i in range(1, len(list)+1) :
#         list1 = list[i-1].split(',')
#         for k in range(1, len(list1)+1) :
#             sheet[chr(k+64) + str(i)].value = list1[k-1]
#     file.save("train_excel.xlsx")
# ex()
#
# for i in f :
#     a = i.replace("0000","")
#     b = a.replace("\t\t",",")
#     c = b.replace("\t","")
#     d = c.replace("\n","")
#     print(d)
#     # f2.write(d+'\n')