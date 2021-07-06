#sbwy foot traffic.py

import pandas as pd
import numpy as np

data = pd.read_csv("subwyfoot.csv")
data1 = data.reset_index()
data1 = data1.drop(['등록일자'],axis=1)
data1.rename(columns = {'index':'사용일자','사용일자':'노선명','노선명':'역명','역명':'승차총승객수','승차총승객수':'하차총승객수','하차총승객수':'요일'},inplace=True)


for i in range(data1.shape[0]):
    if data1.iloc[i,0]%7 == 4:
        data1.iloc[i,5] = '토요일'
    elif data1.iloc[i,0]%7 == 5:
        data1.iloc[i,5] = '일요일'
    elif data1.iloc[i,0]%7 == 6:
        data1.iloc[i,5] = '월요일'
    elif data1.iloc[i,0]%7 == 3:
        data1.iloc[i,5] = '금요일'
    elif data1.iloc[i,0]%7 == 2:
        data1.iloc[i,5] = '목요일'
    elif data1.iloc[i,0]%7 == 1:
        data1.iloc[i,5] = '수요일'
    elif data1.iloc[i,0]%7 == 0:
        data1.iloc[i,5] = '화요일'

line = data1.groupby('노선명')
line1 = line.get_group("1호선")
line2 = line.get_group('2호선')
line3 = line.get_group('3호선')
line4 = line.get_group('4호선')
line5 = line.get_group('5호선')
line6 = line.get_group('6호선')
line7 = line.get_group('7호선')
line8 = line.get_group('8호선')
line9 = line.get_group('9호선')
line23 = line.get_group('9호선2~3단계')
linegyug = line.get_group('경강선')
linegyub = line.get_group('경부선')
linegyuw = line.get_group('경원선')
linegyui = line.get_group('경의선')
linegyun = line.get_group('경인선')
linegyuc = line.get_group('경춘선')
lineair = line.get_group('공항철도 1호선')
linegwua = line.get_group('과천선')
linebun = line.get_group('분당선')
linesuin = line.get_group('수인선')
lineansan = line.get_group('안산선')
linewooi = line.get_group('우이신설선')
lineisan = line.get_group('일산선')
linejang = line.get_group('장항선')
linejung = line.get_group('중앙선')

line1_yoil = line1.groupby('요일')
line1_data = line1_yoil.describe()
line1_data_yoil = (line1_data['승차총승객수','mean']+line1_data['하차총승객수','mean'])/2

line2_yoil = line2.groupby('요일')
line2_data = line2_yoil.describe()
line2_data_yoil = (line2_data['승차총승객수','mean']+line2_data['하차총승객수','mean'])/2

line3_yoil = line3.groupby('요일')
line3_data = line3_yoil.describe()
line3_data_yoil = (line3_data['승차총승객수','mean']+line3_data['하차총승객수','mean'])/2


line4_yoil = line4.groupby('요일')
line4_data = line4_yoil.describe()
line4_data_yoil = (line4_data['승차총승객수','mean']+line4_data['하차총승객수','mean'])/2

line5_yoil = line5.groupby('요일')
line5_data = line5_yoil.describe()
line5_data_yoil = (line5_data['승차총승객수','mean']+line5_data['하차총승객수','mean'])/2

line6_yoil = line6.groupby('요일')
line6_data = line6_yoil.describe()
line6_data_yoil = (line6_data['승차총승객수','mean']+line6_data['하차총승객수','mean'])/2

line7_yoil = line7.groupby('요일')
line7_data = line7_yoil.describe()
line7_data_yoil = (line7_data['승차총승객수','mean']+line7_data['하차총승객수','mean'])/2

line8_yoil = line8.groupby('요일')
line8_data = line8_yoil.describe()
line8_data_yoil = (line8_data['승차총승객수','mean']+line8_data['하차총승객수','mean'])/2

line9_yoil = line9.groupby('요일')
line9_data = line9_yoil.describe()
line9_data_yoil = (line9_data['승차총승객수','mean']+line9_data['승차총승객수','mean'])/2

line23_yoil = line23.groupby('요일')
line23_data = line23_yoil.describe()
line23_data_yoil = (line23_data['승차총승객수','mean']+line23_data['승차총승객수','mean'])/2

linegyug_yoil = linegyug.groupby('요일')
linegyug_data = linegyug_yoil.describe()
linegyug_data_yoil = (linegyug_data['승차총승객수','mean']+linegyug_data['승차총승객수','mean'])/2

linegyub_yoil = linegyub.groupby('요일')
linegyub_data = linegyub_yoil.describe()
linegyub_data_yoil = (linegyub_data['승차총승객수','mean']+linegyub_data['승차총승객수','mean'])/2

linegyuw_yoil = linegyuw.groupby('요일')
linegyuw_data = linegyuw_yoil.describe()
linegyuw_data_yoil = (linegyuw_data['승차총승객수','mean']+linegyuw_data['승차총승객수','mean'])/2

linegyui_yoil = linegyui.groupby('요일')
linegyui_data = linegyui_yoil.describe()
linegyui_data_yoil = (linegyui_data['승차총승객수','mean']+linegyui_data['승차총승객수','mean'])/2

linegyun_yoil = linegyun.groupby('요일')
linegyun_data = linegyun_yoil.describe()
linegyun_data_yoil = (linegyun_data['승차총승객수','mean']+linegyun_data['승차총승객수','mean'])/2

linegyuc_yoil = linegyun.groupby('요일')
linegyuc_data = linegyun_yoil.describe()
linegyuc_data_yoil = (linegyun_data['승차총승객수','mean']+linegyun_data['승차총승객수','mean'])/2

lineair_yoil = lineair.groupby('요일')
lineair_data = lineair_yoil.describe()
lineair_data_yoil = (lineair_data['승차총승객수','mean']+lineair_data['승차총승객수','mean'])/2

linegwua_yoil = linegwua.groupby('요일')
linegwua_data = linegwua_yoil.describe()
linegwua_data_yoil = (linegwua_data['승차총승객수','mean']+linegwua_data['승차총승객수','mean'])/2

linebun_yoil = linebun.groupby('요일')
linebun_data = linebun_yoil.describe()
linebun_data_yoil = (linebun_data['승차총승객수','mean']+linebun_data['승차총승객수','mean'])/2

linesuin_yoil = linesuin.groupby('요일')
linesuin_data = linesuin_yoil.describe()
linesuin_data_yoil = (linesuin_data['승차총승객수','mean']+linesuin_data['승차총승객수','mean'])/2

lineansan_yoil = lineansan.groupby('요일')
lineansan_data = lineansan_yoil.describe()
lineansan_data_yoil = (lineansan_data['승차총승객수','mean']+lineansan_data['승차총승객수','mean'])/2

linewooi_yoil = linewooi.groupby('요일')
linewooi_data = linewooi_yoil.describe()
linewooi_data_yoil = (linewooi_data['승차총승객수','mean']+linewooi_data['승차총승객수','mean'])/2

lineisan_yoil = lineisan.groupby('요일')
lineisan_data = lineisan_yoil.describe()
lineisan_data_yoil = (lineisan_data['승차총승객수','mean']+lineisan_data['승차총승객수','mean'])/2

linejang_yoil = linejang.groupby('요일')
linejang_data = linejang_yoil.describe()
linejang_data_yoil = (linejang_data['승차총승객수','mean']+linejang_data['승차총승객수','mean'])/2

linejung_yoil = linejung.groupby('요일')
linejung_data = linejung_yoil.describe()
linejung_data_yoil = (linejung_data['승차총승객수','mean']+linejung_data['승차총승객수','mean'])/2


temp = data1.sample(frac=1).reset_index(drop=True)
x = round(data1.shape[0]/100)
data2 = temp[0:x]


for i in range(x):
    if data2.iloc[i,1] == '5호선' and data2.iloc[i,5] == '토요일':
        if line5_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line5_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > line5_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line5_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '5호선' and data2.iloc[i,5] == '일요일':
        if line5_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line5_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > line5_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line5_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '5호선' and data2.iloc[i,5] == '월요일':
        if line5_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line5_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > line5_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line5_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '5호선' and data2.iloc[i,5] == '화요일':
        if line5_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line5_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > line5_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line5_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '5호선' and data2.iloc[i,5] == '수요일':
        if line5_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line5_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > line5_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line5_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '5호선' and data2.iloc[i,5] == '목요일':
        if line5_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line5_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > line5_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line5_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '5호선' and data2.iloc[i,5] == '금요일':
        if line5_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line5_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > line5_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line5_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')

            
    if data2.iloc[i,1] == '4호선' and data2.iloc[i,5] == '토요일':
        if line4_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line4_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > line4_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line4_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '4호선' and data2.iloc[i,5] == '일요일':
        if line4_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line4_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > line4_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line4_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '4호선' and data2.iloc[i,5] == '월요일':
        if line4_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line4_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > line4_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line4_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '4호선' and data2.iloc[i,5] == '화요일':
        if line4_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line4_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > line4_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line4_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '4호선' and data2.iloc[i,5] == '수요일':
        if line4_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line4_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > line4_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line4_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '4호선' and data2.iloc[i,5] == '목요일':
        if line4_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line4_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > line4_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line4_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '4호선' and data2.iloc[i,5] == '금요일':
        if line4_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line4_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > line4_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line4_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
            
    if data2.iloc[i,1] == '3호선' and data2.iloc[i,5] == '토요일':
        if line3_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line3_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > line3_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line3_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '3호선' and data2.iloc[i,5] == '일요일':
        if line3_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line3_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > line3_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line3_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '3호선' and data2.iloc[i,5] == '월요일':
        if line3_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line3_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > line3_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line3_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '3호선' and data2.iloc[i,5] == '화요일':
        if line3_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line3_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > line3_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line3_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '3호선' and data2.iloc[i,5] == '수요일':
        if line3_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line3_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > line3_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line3_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '3호선' and data2.iloc[i,5] == '목요일':
        if line3_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line3_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > line3_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line3_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '3호선' and data2.iloc[i,5] == '금요일':
        if line3_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line3_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > line3_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line3_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
            
    if data2.iloc[i,1] == '2호선' and data2.iloc[i,5] == '토요일':
        if line2_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line2_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > line2_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line2_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '2호선' and data2.iloc[i,5] == '일요일':
        if line2_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line2_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > line2_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line2_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '2호선' and data2.iloc[i,5] == '월요일':
        if line2_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line2_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > line2_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line2_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '2호선' and data2.iloc[i,5] == '화요일':
        if line2_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line2_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > line2_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line2_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '2호선' and data2.iloc[i,5] == '수요일':
        if line2_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line2_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > line2_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line2_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '2호선' and data2.iloc[i,5] == '목요일':
        if line2_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line2_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > line2_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line2_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '2호선' and data2.iloc[i,5] == '금요일':
        if line2_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line2_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > line2_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line2_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    
    if data2.iloc[i,1] == '1호선' and data2.iloc[i,5] == '토요일':
        if line1_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line1_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > line1_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line1_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '1호선' and data2.iloc[i,5] == '일요일':
        if line1_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line1_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > line1_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line1_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '1호선' and data2.iloc[i,5] == '월요일':
        if line1_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line1_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > line1_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line1_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '1호선' and data2.iloc[i,5] == '화요일':
        if line1_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line1_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > line1_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line1_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '1호선' and data2.iloc[i,5] == '수요일':
        if line1_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line1_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > line1_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line1_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '1호선' and data2.iloc[i,5] == '목요일':
        if line1_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line1_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > line1_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line1_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '1호선' and data2.iloc[i,5] == '금요일':
        if line1_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line1_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > line1_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line1_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
            
    if data2.iloc[i,1] == '6호선' and data2.iloc[i,5] == '토요일':
        if line6_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line6_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > line6_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line6_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '6호선' and data2.iloc[i,5] == '일요일':
        if line6_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line6_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > line6_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line6_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '6호선' and data2.iloc[i,5] == '월요일':
        if line6_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line6_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > line6_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line6_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '6호선' and data2.iloc[i,5] == '화요일':
        if line6_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line6_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > line6_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line6_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '6호선' and data2.iloc[i,5] == '수요일':
        if line6_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line6_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > line6_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line6_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '6호선' and data2.iloc[i,5] == '목요일':
        if line6_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line6_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > line6_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line6_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '6호선' and data2.iloc[i,5] == '금요일':
        if line6_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line6_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > line6_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line6_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    
    if data2.iloc[i,1] == '7호선' and data2.iloc[i,5] == '토요일':
        if line7_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line7_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > line7_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line7_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '7호선' and data2.iloc[i,5] == '일요일':
        if line7_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line7_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > line7_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line7_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '7호선' and data2.iloc[i,5] == '월요일':
        if line7_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line7_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > line7_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line7_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '7호선' and data2.iloc[i,5] == '화요일':
        if line7_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line7_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > line7_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line7_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '7호선' and data2.iloc[i,5] == '수요일':
        if line7_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line7_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > line7_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line7_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '7호선' and data2.iloc[i,5] == '목요일':
        if line7_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line7_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > line7_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line7_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '7호선' and data2.iloc[i,5] == '금요일':
        if line7_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line7_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > line7_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line7_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')

    if data2.iloc[i,1] == '8호선' and data2.iloc[i,5] == '토요일':
        if line8_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line8_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > line8_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line8_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '8호선' and data2.iloc[i,5] == '일요일':
        if line8_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line8_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > line8_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line8_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '8호선' and data2.iloc[i,5] == '월요일':
        if line8_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line8_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > line8_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line8_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '8호선' and data2.iloc[i,5] == '화요일':
        if line8_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line8_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > line8_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line8_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '8호선' and data2.iloc[i,5] == '수요일':
        if line8_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line8_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > line8_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line8_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '8호선' and data2.iloc[i,5] == '목요일':
        if line8_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line8_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > line8_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line8_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')      
    elif data2.iloc[i,1] == '8호선' and data2.iloc[i,5] == '금요일':
        if line8_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line8_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > line8_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line8_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
            
    if data2.iloc[i,1] == '9호선' and data2.iloc[i,5] == '토요일':
        if line9_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line9_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > line9_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line9_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '9호선' and data2.iloc[i,5] == '일요일':
        if line9_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line9_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > line9_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line9_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '9호선' and data2.iloc[i,5] == '월요일':
        if line9_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line9_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > line9_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line9_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '9호선' and data2.iloc[i,5] == '화요일':
        if line9_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line9_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > line9_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line9_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '9호선' and data2.iloc[i,5] == '수요일':
        if line9_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line9_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > line9_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line9_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '9호선' and data2.iloc[i,5] == '목요일':
        if line9_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line9_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > line9_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line9_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '9호선' and data2.iloc[i,5] == '금요일':
        if line9_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line9_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > line9_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line9_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')

    if data2.iloc[i,1] == '9호선2~단계' and data2.iloc[i,5] == '토요일':
        if line23_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line23_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > line23_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line23_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '9호선2~단계' and data2.iloc[i,5] == '일요일':
        if line23_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line23_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > line23_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line23_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '9호선2~단계' and data2.iloc[i,5] == '월요일':
        if line23_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line23_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > line23_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line23_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '9호선2~단계' and data2.iloc[i,5] == '화요일':
        if line23_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line23_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > line23_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line23_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '9호선2~단계' and data2.iloc[i,5] == '수요일':
        if line23_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line23_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > line23_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line23_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '9호선2~단계' and data2.iloc[i,5] == '목요일':
        if line23_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line23_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > line23_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line23_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '9호선2~단계' and data2.iloc[i,5] == '금요일':
        if line23_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif line23_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > line23_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif line23_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
            
    if data2.iloc[i,1] == '경부선' and data2.iloc[i,5] == '토요일':
        if linegyub_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyub_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > linegyub_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyub_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경부선' and data2.iloc[i,5] == '일요일':
        if linegyub_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyub_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > linegyub_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyub_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경부선' and data2.iloc[i,5] == '월요일':
        if linegyub_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyub_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > linegyub_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyub_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경부선' and data2.iloc[i,5] == '화요일':
        if linegyub_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyub_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > linegyub_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyub_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경부선' and data2.iloc[i,5] == '수요일':
        if linegyub_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyub_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > linegyub_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyub_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경부선' and data2.iloc[i,5] == '목요일':
        if linegyub_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyub_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > linegyub_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyub_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경부선' and data2.iloc[i,5] == '금요일':
        if linegyub_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyub_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > linegyub_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyub_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')


    if data2.iloc[i,1] == '경강선' and data2.iloc[i,5] == '토요일':
        if linegyug_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyug_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > linegyug_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyug_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경강선' and data2.iloc[i,5] == '일요일':
        if linegyug_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyug_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > linegyug_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyug_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경강선' and data2.iloc[i,5] == '월요일':
        if linegyug_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyug_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > linegyug_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyug_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경강선' and data2.iloc[i,5] == '화요일':
        if linegyug_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyug_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > linegyug_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyug_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경강선' and data2.iloc[i,5] == '수요일':
        if linegyug_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyug_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > linegyug_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyug_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경강선' and data2.iloc[i,5] == '목요일':
        if linegyug_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyug_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > linegyug_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyug_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경강선' and data2.iloc[i,5] == '금요일':
        if linegyug_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyug_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > linegyug_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyug_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')


    if data2.iloc[i,1] == '경의선' and data2.iloc[i,5] == '토요일':
        if linegyui_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyui_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > linegyui_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyui_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경의선' and data2.iloc[i,5] == '일요일':
        if linegyui_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyui_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > linegyui_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyui_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경의선' and data2.iloc[i,5] == '월요일':
        if linegyui_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyui_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > linegyui_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyui_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경의선' and data2.iloc[i,5] == '화요일':
        if linegyui_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyui_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > linegyui_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyui_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경의선' and data2.iloc[i,5] == '수요일':
        if linegyui_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyui_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > linegyui_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyui_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경의선' and data2.iloc[i,5] == '목요일':
        if linegyui_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyui_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > linegyui_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyui_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경의선' and data2.iloc[i,5] == '금요일':
        if linegyui_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyui_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > linegyui_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyui_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')

    if data2.iloc[i,1] == '경인선' and data2.iloc[i,5] == '토요일':
        if linegyun_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyun_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > linegyun_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyun_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경인선' and data2.iloc[i,5] == '일요일':
        if linegyun_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyun_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > linegyun_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyun_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경인선' and data2.iloc[i,5] == '월요일':
        if linegyun_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyun_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > linegyun_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyun_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경인선' and data2.iloc[i,5] == '화요일':
        if linegyun_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyun_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > linegyun_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyun_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경인선' and data2.iloc[i,5] == '수요일':
        if linegyun_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyun_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > linegyun_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyun_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경인선' and data2.iloc[i,5] == '목요일':
        if linegyun_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyun_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > linegyun_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyun_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경인선' and data2.iloc[i,5] == '금요일':
        if linegyun_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyun_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > linegyun_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyun_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')

    if data2.iloc[i,1] == '경춘선' and data2.iloc[i,5] == '토요일':
        if linegyuc_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyuc_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > linegyuc_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyuc_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경춘선' and data2.iloc[i,5] == '일요일':
        if linegyuc_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyuc_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > linegyuc_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyuc_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경춘선' and data2.iloc[i,5] == '월요일':
        if linegyuc_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyuc_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > linegyuc_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyuc_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경춘선' and data2.iloc[i,5] == '화요일':
        if linegyuc_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyuc_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > linegyuc_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyuc_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경춘선' and data2.iloc[i,5] == '수요일':
        if linegyuc_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyuc_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > linegyuc_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyuc_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경춘선' and data2.iloc[i,5] == '목요일':
        if linegyuc_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyuc_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > linegyuc_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyuc_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경춘선' and data2.iloc[i,5] == '금요일':
        if linegyuc_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyuc_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > linegyuc_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyuc_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')

    if data2.iloc[i,1] == '공항철도 1호선' and data2.iloc[i,5] == '토요일':
        if lineair_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineair_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > lineair_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineair_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '공항철도 1호선' and data2.iloc[i,5] == '일요일':
        if lineair_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineair_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > lineair_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineair_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '공항철도 1호선' and data2.iloc[i,5] == '월요일':
        if lineair_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineair_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > lineair_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineair_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '공항철도 1호선' and data2.iloc[i,5] == '화요일':
        if lineair_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineair_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > lineair_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineair_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '공항철도 1호선' and data2.iloc[i,5] == '수요일':
        if lineair_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineair_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > lineair_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineair_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '공항철도 1호선' and data2.iloc[i,5] == '목요일':
        if lineair_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineair_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > lineair_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineair_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '공항철도 1호선' and data2.iloc[i,5] == '금요일':
        if lineair_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineair_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > lineair_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineair_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')


    if data2.iloc[i,1] == '과천선' and data2.iloc[i,5] == '토요일':
        if linegwua_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegwua_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > linegwua_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegwua_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '과천선' and data2.iloc[i,5] == '일요일':
        if linegwua_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegwua_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > linegwua_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegwua_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '과천선' and data2.iloc[i,5] == '월요일':
        if linegwua_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegwua_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > linegwua_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegwua_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '과천선' and data2.iloc[i,5] == '화요일':
        if linegwua_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegwua_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > linegwua_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegwua_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '과천선' and data2.iloc[i,5] == '수요일':
        if linegwua_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegwua_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > linegwua_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegwua_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '과천선' and data2.iloc[i,5] == '목요일':
        if linegwua_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegwua_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > linegwua_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegwua_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '과천선' and data2.iloc[i,5] == '금요일':
        if linegwua_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegwua_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > linegwua_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegwua_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')


    if data2.iloc[i,1] == '분당선' and data2.iloc[i,5] == '토요일':
        if linebun_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linebun_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > linebun_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linebun_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '분당선' and data2.iloc[i,5] == '일요일':
        if linebun_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linebun_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > linebun_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linebun_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '분당선' and data2.iloc[i,5] == '월요일':
        if linebun_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linebun_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > linebun_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linebun_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '분당선' and data2.iloc[i,5] == '화요일':
        if linebun_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linebun_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > linebun_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linebun_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '분당선' and data2.iloc[i,5] == '수요일':
        if linebun_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linebun_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > linebun_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linebun_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '분당선' and data2.iloc[i,5] == '목요일':
        if linebun_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linebun_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > linebun_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linebun_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '분당선' and data2.iloc[i,5] == '금요일':
        if linebun_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linebun_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > linebun_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linebun_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')


    if data2.iloc[i,1] == '수인선' and data2.iloc[i,5] == '토요일':
        if linesuin_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linesuin_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > linesuin_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linesuin_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '수인선' and data2.iloc[i,5] == '일요일':
        if linesuin_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linesuin_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > linesuin_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linesuin_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '수인선' and data2.iloc[i,5] == '월요일':
        if linesuin_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linesuin_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > linesuin_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linesuin_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '수인선' and data2.iloc[i,5] == '화요일':
        if linesuin_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linesuin_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > linesuin_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linesuin_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '수인선' and data2.iloc[i,5] == '수요일':
        if linesuin_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linesuin_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > linesuin_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linesuin_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '수인선' and data2.iloc[i,5] == '목요일':
        if linesuin_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linesuin_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > linesuin_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linesuin_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '수인선' and data2.iloc[i,5] == '금요일':
        if linesuin_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linesuin_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > linesuin_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linesuin_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')


    if data2.iloc[i,1] == '안산선' and data2.iloc[i,5] == '토요일':
        if lineansan_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineansan_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > lineansan_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineansan_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '안산선' and data2.iloc[i,5] == '일요일':
        if lineansan_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineansan_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > lineansan_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineansan_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '안산선' and data2.iloc[i,5] == '월요일':
        if lineansan_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineansan_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > lineansan_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineansan_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '안산선' and data2.iloc[i,5] == '화요일':
        if lineansan_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineansan_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > lineansan_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineansan_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '안산선' and data2.iloc[i,5] == '수요일':
        if lineansan_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineansan_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > lineansan_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineansan_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '안산선' and data2.iloc[i,5] == '목요일':
        if lineansan_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineansan_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > lineansan_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineansan_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '안산선' and data2.iloc[i,5] == '금요일':
        if lineansan_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineansan_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > lineansan_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineansan_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')


    if data2.iloc[i,1] == '우이신설선' and data2.iloc[i,5] == '토요일':
        if linewooi_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linewooi_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > linewooi_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linewooi_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '우이신설선' and data2.iloc[i,5] == '일요일':
        if linewooi_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linewooi_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > linewooi_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linewooi_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '우이신설선' and data2.iloc[i,5] == '월요일':
        if linewooi_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linewooi_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > linewooi_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linewooi_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '우이신설선' and data2.iloc[i,5] == '화요일':
        if linewooi_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linewooi_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > linewooi_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linewooi_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '우이신설선' and data2.iloc[i,5] == '수요일':
        if linewooi_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linewooi_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > linewooi_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linewooi_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '우이신설선' and data2.iloc[i,5] == '목요일':
        if linewooi_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linewooi_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > linewooi_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linewooi_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '우이신설선' and data2.iloc[i,5] == '금요일':
        if linewooi_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linewooi_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > linewooi_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linewooi_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')


    if data2.iloc[i,1] == '일산선' and data2.iloc[i,5] == '토요일':
        if lineisan_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineisan_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > lineisan_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineisan_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '일산선' and data2.iloc[i,5] == '일요일':
        if lineisan_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineisan_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > lineisan_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineisan_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '일산선' and data2.iloc[i,5] == '월요일':
        if lineisan_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineisan_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > lineisan_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineisan_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '일산선' and data2.iloc[i,5] == '화요일':
        if lineisan_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineisan_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > lineisan_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineisan_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '일산선' and data2.iloc[i,5] == '수요일':
        if lineisan_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineisan_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > lineisan_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineisan_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '일산선' and data2.iloc[i,5] == '목요일':
        if lineisan_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineisan_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > lineisan_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineisan_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '일산선' and data2.iloc[i,5] == '금요일':
        if lineisan_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif lineisan_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > lineisan_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif lineisan_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')


    if data2.iloc[i,1] == '장항선' and data2.iloc[i,5] == '토요일':
        if linejang_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linejang_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > linejang_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linejang_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '장항선' and data2.iloc[i,5] == '일요일':
        if linejang_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linejang_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > linejang_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linejang_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '장항선' and data2.iloc[i,5] == '월요일':
        if linejang_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linejang_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > linejang_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linejang_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '장항선' and data2.iloc[i,5] == '화요일':
        if linejang_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linejang_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > linejang_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linejang_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '장항선' and data2.iloc[i,5] == '수요일':
        if linejang_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linejang_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > linejang_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linejang_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '장항선' and data2.iloc[i,5] == '목요일':
        if linejang_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linejang_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > linejang_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linejang_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '장항선' and data2.iloc[i,5] == '금요일':
        if linejang_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linejang_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > linejang_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linejang_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')

    if data2.iloc[i,1] == '중앙선' and data2.iloc[i,5] == '토요일':
        if linejung_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linejung_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > linejung_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linejung_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '중앙선' and data2.iloc[i,5] == '일요일':
        if linejung_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linejung_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > linejung_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linejung_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '중앙선' and data2.iloc[i,5] == '월요일':
        if linejung_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linejung_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > linejung_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linejung_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '중앙선' and data2.iloc[i,5] == '화요일':
        if linejung_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linejung_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > linejung_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linejung_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '중앙선' and data2.iloc[i,5] == '수요일':
        if linejung_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linejung_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > linejung_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linejung_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '중앙선' and data2.iloc[i,5] == '목요일':
        if linejung_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linejung_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > linejung_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linejung_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '중앙선' and data2.iloc[i,5] == '금요일':
        if linejung_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linejung_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > linejung_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linejung_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')

    if data2.iloc[i,1] == '경원선' and data2.iloc[i,5] == '토요일':
        if linegyuw_data_yoil.loc['토요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyuw_data_yoil.loc['토요일']*1.2 > data2.iloc[i,3] > linegyuw_data_yoil.loc['토요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyuw_data_yoil.loc['토요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경원선' and data2.iloc[i,5] == '일요일':
        if linegyuw_data_yoil.loc['일요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyuw_data_yoil.loc['일요일']*1.2 > data2.iloc[i,3] > linegyuw_data_yoil.loc['일요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyuw_data_yoil.loc['일요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경원선' and data2.iloc[i,5] == '월요일':
        if linegyuw_data_yoil.loc['월요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyuw_data_yoil.loc['월요일']*1.2 > data2.iloc[i,3] > linegyuw_data_yoil.loc['월요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyuw_data_yoil.loc['월요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경원선' and data2.iloc[i,5] == '화요일':
        if linegyuw_data_yoil.loc['화요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyuw_data_yoil.loc['화요일']*1.2 > data2.iloc[i,3] > linegyuw_data_yoil.loc['화요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyuw_data_yoil.loc['화요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경원선' and data2.iloc[i,5] == '수요일':
        if linegyuw_data_yoil.loc['수요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyuw_data_yoil.loc['수요일']*1.2 > data2.iloc[i,3] > linegyuw_data_yoil.loc['수요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyuw_data_yoil.loc['수요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경원선' and data2.iloc[i,5] == '목요일':
        if linegyuw_data_yoil.loc['목요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyuw_data_yoil.loc['목요일']*1.2 > data2.iloc[i,3] > linegyuw_data_yoil.loc['목요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyuw_data_yoil.loc['목요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')
    elif data2.iloc[i,1] == '경원선' and data2.iloc[i,5] == '금요일':
        if linegyuw_data_yoil.loc['금요일']*1.2 < data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':혼잡')
        elif linegyuw_data_yoil.loc['금요일']*1.2 > data2.iloc[i,3] > linegyuw_data_yoil.loc['금요일']*0.8:
            print(data2.iloc[i,0:3].values,':보통')
        elif linegyuw_data_yoil.loc['금요일']*0.8 > data2.iloc[i,3]:
            print(data2.iloc[i,0:3].values,':여유')


