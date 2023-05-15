import docx
import pandas as pd

doc = docx.Document('E:/综合事务/2022年考生分档表.docx')
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

number = number[0: 2724]

df = pd.DataFrame({'number':number, 'name':name, 'grade':grade})
df.to_csv('E:/output.csv', encoding= 'GBK', index= False)