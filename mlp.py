from scipy import optimize as op
import numpy as np
import pandas as pd
from scipy.optimize import linprog


original = pd.read_excel(r"C:\Users\EDZ\Documents\WeChat Files\wxid_ei9t613c18zd22\FileStorage\File\2021-06\2021年4月青海送陕西月度省间外送交易无约束交易结果.xlsx",
                     skiprows = [0,1])
data_sell = {}
data_buy = {}
for i in original.售方名称.unique():
    temp = []
    for j in original[original['售方名称']=='尼那电厂'].售方电量:
        j /= 32
        temp.append(j)
    data_sell['{}'.format(i)] = [val for val in temp for num in range(32)]
for i in [chr(i) for i in range(97, 123)]:
    temp = []
    temp.append(np.random.normal(17,0.5))
    temp.append(np.random.normal(19,0.5))
    temp.append(np.random.normal(18,0.5))
    temp = [val for val in temp for num in range(32)]
    data_buy["{}".format(i)] = temp
a_ed = []
for key in data_buy.keys():
    a_ed.append(data_buy[key])
a_ed = np.array(a_ed).T
b_ed = np.array(data_sell['公伯峡电厂'])
a_ed = np.c_[a_ed,b_ed.T]
c = np.random.normal(200,10,27)*a_ed.sum(axis=0)
result = linprog(c, A_eq = a_ed,  b_eq = b_ed, bounds=([[0,1]]*27))
# c = np.random.normal(200,10,26)*a_ed.sum(axis=0)
# result = linprog(c, A_eq = a_ed,  b_eq = b_ed, bounds=([[0,1]]*26))
print(result)
print('')