#승차 승객수의 역별 평균을 구하고, 평균값과 사용일자별 값을 비교하여 많고 적음 분류
import pandas as pd
import numpy as np
from numpy import NaN, dtype
df = pd.read_csv('asdf.py/sub1.csv')    #사용일자와 등록일자를 삭제하고 오름차순으로 정리한 파일
df_unique = df['역명'].unique() #unique,df에서 '역명'의 고유값만 저장 (278,0)
df_unique = pd.DataFrame(df_unique) #ndarray to dataframe
df_mean = [[NaN for j in range(100)] for i in range(278)]   #역명별 평균을 구하기 위한 역별 승객수를 저장하기 위한 list

i = 0 #i초기화
j = 0   #j,i와 동일하게 동작 저장할 값의 행
for i in df_unique[0]:
    n = 0
    l = 0   #저장 값의 열
    for k in df['역명']:    #n,k와 동일하게 동작
        if i == k:
           df_mean[j][l] = df.loc[n][2] #loc,인덱스 기준으로 행 읽기
           l += 1
        n += 1
    j += 1 
df_mean = pd.DataFrame(df_mean) #list to dataframe
df_mean = np.transpose(df_mean)    # dataframe transform
df_mean = df_mean.mean()   # mean per columns
df_result = pd.concat([df_unique,df_mean],axis=1) #df_result=역명,평균의 dataframe병합
df_result.columns = [0,1]
df1 = [[NaN for j in range(9897)]] # 분류결과저장
i = 0   #i초기화
k = 0
j = 0   #j,i와 동일하게 동작 저장할 값의 행
for i in df_result[0]:
    n = 0
    for k in df['역명']:    #n,k와 동일하게 동작
        if i == k:
            if df_result.loc[j][1] < df.loc[n][2]: #loc,인덱스 기준으로 행 읽기
               df1[0][n] = '많음' 
            elif df_result.loc[j][1] == df.loc[n][2]:
                df1[0][n] = '보통'
            else:
               df1[0][n] = '적음'
        n += 1
    j += 1 
df1 = pd.DataFrame(df1)
df1 = np.transpose(df1)
df1 = pd.concat([df,df1],axis=1)    #df와 df1병합
print(df1)
# 데이터 2개 누락
# 승차인원에 대한 결과만 조사
# 요일별 분류와 이용자 수가 많고 적음을 나누는 기준 세분화 필요