import pandas as pd

data_1 = pd.read_excel(r"C:\Users\EDZ\Desktop\数据维护\超短期交易_20210525 (3).xlsx",dtype={'交易ID':'str'})
data_2 = pd.read_excel(r"C:\Users\EDZ\Desktop\数据维护\日清月结数据202104(1-30日)(日前实时跟踪）(5.9).xls",sheet_name = '日前实时清单')
data_2 = data_2[data_2['交易日']==1]
id_1 = data_1['交易ID'].unique()
id_2 = data_2['交易ID'].unique()
diff = []
for i in id_1:
    if i not in id_2:
        diff.append(i)
diff_2 = {}
for i in id_2:
    temp_1 = data_1[data_1['交易ID']==i]['电量(万kWh)'].sum()
    temp_2 = data_2[data_2['交易ID']==i]['电量(万kWh)'].sum()
    if temp_1!=temp_2 and abs(temp_1-temp_2)>0.01:
        diff_2[i] = [temp_1,temp_2]

print('')