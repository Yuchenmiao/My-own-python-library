import docx
import pandas as pd

doc = docx.Document('E:/综合事务/2023年考生分档情况.docx')
text = ''
for para in doc.paragraphs:
    text += para.text + '\n'

text_list = text.split('\n')

number = []
name = []
grade = []

for i in range(3, len(text_list)) :
    if i % 3 == 0 :
        number.append(text_list[i])
    elif i % 3 == 1 :
        name.append(text_list[i])
    else :
        grade.append(text_list[i])

length = min(len(number), len(name), len(grade))
number = number[0:length]
name = name[0:length]
grade = grade[0:length]

df = pd.DataFrame({'number':number, 'name':name, 'grade':grade})
df.to_csv('E:/综合事务/2023级上科大新生分档情况表.csv', encoding= 'GBK', index= False)