import random
import pandas as pd
data = pd.read_excel(r"C:\Users\EDZ\Documents\WeChat Files\wxid_ei9t613c18zd22\FileStorage\File\2021-05\名单(1).xlsx")
data = list(data['参加人员'].values)
a = 0
num = 0
temp_group = []
while num < 4:
    temp_person = random.choice(data)
    data.remove(temp_person)
    temp_group.append(temp_person)
    a += 1
    if a==10 and num!=3 :
        print("第{}组成员为:".format(num+1),temp_group)
        num += 1
        a = 0
        temp_group = []
    elif a>10 :
        print("第{}组成员为:".format(num + 1), temp_group)
        num += 1



