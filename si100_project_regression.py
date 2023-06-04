import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.api as sm

df = pd.read_excel(r'E:\大一下学期\SI100\Project\cv信息的提取_汇总_新_带领域(最终版本).xlsx')
groups = df.groupby(df.columns[2])
fields = {
    'Economics of Education': 'education',
    'Applied Microeconomics': 'micro',
    'Labor Economics': 'labor',
    'Environment Economics': 'environ',
    'Public Economics': 'public',
    'Macroeconomics': 'macro',
    'Behavioral Economics': 'behav',
    'Political Economics': 'poli',
    'International Trade': 'trade'or'inter',
    'Regional Economics': 'region',
    'Finance': 'finan',
    'Industrial Organization': 'organization',
    'Game Theory': 'game',
    'Monetary Economics': 'monetary',
    'Urban Economics': 'urban',
    'Econometrics': 'econometrics',
    'Mathematical Economics': 'math',
    'Health Economics': 'health',
    'Economics of Population': 'popu'
}

result = []
for group_name, data in groups:
    data_str = ','.join(data[data.columns[4]].astype(str))
    data_str = data_str.lower()
    GDP = data[data.columns[3]].unique().astype(int)
    GDP = GDP.item()
    GDP = GDP / 10000
    pop = data[data.columns[5]].unique().astype(int)
    pop = pop.item()
    pop = pop / 1000000
    field_counts = {field: 0 for field in fields}
    
    for field, keyword in fields.items():
        count = data_str.count(keyword)
        field_counts[field] += count

    score = 0
    for field, count in field_counts.items():
        if field == 'Economics of Education':
            score += 5 * count
        elif field == 'Applied Microeconomics':
            score += 5 * count
        elif field == 'Labor Economics':
            score += 5 * count
        elif field == 'Environment Economics':
            score += 4 * count
        elif field == 'Public Economics':
            score += 4 * count
        elif field == 'Macroeconomics':
            score += 8 * count
        elif field == 'Behavioral Economics':
            score += 4 * count
        elif field == 'Political Economics':
            score += 3 * count
        elif field == 'International Trade':
            score += 6 * count
        elif field == 'Regional Economics':
            score += 2 * count
        elif field == 'Finance':
            score += 7 * count
        elif field == 'Industrial Organization':
            score += 7 * count
        elif field == 'Game Theory':
            score += 7 * count
        elif field == 'Monetary Economics':
            score += 8 * count
        elif field == 'Urban Economics':
            score += 4 * count
        elif field == 'Econometrics':
            score += 10 * count
        elif field == 'Mathematical Economics':
            score += 10 * count
        elif field == 'Health Economics':
            score += 4 * count
        elif field == 'Economics of Population':
            score += 4 * count

    line_count = len(data)
    data_count = sum(len(item.split(',')) for item in data[data.columns[4]].astype(str))

    result.append({'国家': group_name, '人数': len(data), '国家得分均值': score / data_count, '人均GDP(万美元)': GDP, '人口(百万人)': pop})

result_df = pd.DataFrame(result)
print(result_df)
column_names = result_df.columns
plt.scatter(result_df[column_names[3]], result_df[column_names[2]], s=result_df[column_names[1]], alpha=0.5)
plt.show()

variables = result_df.iloc[:, [3, 4]].values
y = result_df.iloc[:, 2].values
variables = sm.add_constant(variables)
model = sm.OLS(y, variables)
results = model.fit()
print(results.summary())