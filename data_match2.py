import pandas as pd
import numpy as np
data = pd.read_excel(r"C:\Users\EDZ\Desktop\数据维护\5月份.xls")
data.replace('<NULL>',np.nan,inplace = True)
# data['交易结果量'] = data['交易结果量'].astype('float')
# data['有约束两'] = data['有约束两'].astype('float')
# data['无约束量'] = data['无约束量'].astype('float')
# data['交易计划量'] = data['交易计划量'].astype('float')
error = {}
for i in data.index:
    if data.loc[i, '有约束两'] is np.nan:
        if data.loc[i,'无约束量'] is np.nan:
            continue
        elif data.loc[i,'无约束量'] != data.loc[i,'交易结果量']:
            error[data.loc[i, '合同名称']] = [data.loc[i, '交易结果量'], data.loc[i, '有约束两'], data.loc[i, '无约束量'],
                                          data.loc[i, '交易计划量']]
    elif data.loc[i,'有约束两'] != data.loc[i,'交易结果量']:
        error[data.loc[i, '合同名称']] = [data.loc[i, '交易结果量'], data.loc[i, '有约束两'], data.loc[i, '无约束量'],
                                      data.loc[i, '交易计划量']]
print('')