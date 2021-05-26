import pandas as pd

data_1 = pd.read_excel(r"C:\Users\EDZ\Desktop\数据维护\超短期交易_4月.xlsx",dtype={'交易ID':'str'})
data_1['标记'] = ['正常']*len(data_1)
data_2 = pd.read_excel(r"C:\Users\EDZ\Desktop\数据维护\超短期4月线下.xlsx")
data_2['标记'] = ['正常']*len(data_2)
id_1 = list(data_1['交易ID'].unique())
id_2 = list(data_2['交易ID'].unique())
same = [i for i in id_1 if i in id_2]
diff_1_2 = [i for i in id_1 if i not in id_2]   #表1比表2多出的部分
diff_2_1 = [i for i in id_2 if i not in id_1]   #表2比表1多出的部分
diff = {}
for i in same:
    temp_1 = data_1[data_1['交易ID']==i]['电量(万kWh)'].sum()
    temp_2 = data_2[data_2['交易ID']==i]['电量(万kWh)'].sum()
    if temp_1!=temp_2 and abs(temp_1-temp_2)>0.01:
        diff[i] = [temp_1,temp_2]
for i in diff_1_2:
    data_1.loc[data_1[data_1['交易ID']==i].index.values,'标记'] = '多余'
for i in diff_2_1:
    data_2.loc[data_2[data_2['交易ID']==i].index.values,'标记'] = '多余'
for i in diff:
    data_1.loc[data_1[data_1['交易ID']==i].index.values,'标记'] = '不同'
    data_2.loc[data_2[data_2['交易ID']==i].index.values,'标记'] = '不同'
data_1.to_excel(r'4月份超短期线上交易数据.xlsx')
data_2.to_excel(r'4月份超短期线下交易数据.xlsx')
print('')