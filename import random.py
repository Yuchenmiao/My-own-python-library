import random
from openpyxl import Workbook

# 创建工作簿对象
workbook = Workbook()

# 获取当前工作表
sheet = workbook.active

# 生成10*10的随机数表，范围是70-95
random_table = [[random.randint(70, 95) for _ in range(10)] for _ in range(10)]

# 将随机数表写入工作表
for i, row in enumerate(random_table, start=1):
    for j, value in enumerate(row, start=1):
        sheet.cell(row=i, column=j, value=value)

# 保存工作簿
workbook.save(filename='C:/Users/18063/Desktop/random_table.xlsx')