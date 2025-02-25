import pandas as pd

df=pd.read_excel('/Users/lxjarctane2/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/f98114c2f05a02f01a0dbf71e38dcfec/Message/MessageTemp/d876688d5ca795bd3c35f21f623c7796/File/gold_input_data.xlsx',sheet_name='Sheet1',engine='openpyxl')

df.info()

y_lt=[2024,2020,2016,2012,2008,2004,2000,1996]

medal=[]
host=[]
Par=[]
year=[]
NOC=[]
PerMedal=[]
DOM=[]
PerGold=[]


dfi = df[df['Year'] == 2024]

set_med = set(dfi['Medal'])

list_med = list(set_med)

list_med = sorted(list_med, reverse=True)

top10_med=list_med[0:10]

top10_noc=[]

for i in top10_med:
    dfi2=dfi[dfi['Medal']==i]
    top10_noc.extend(list(set(dfi2['NOC'])))


noc_sum=set(df['NOC'])

noc_sum.difference_update(set(top10_noc))

NOC_lt=list(noc_sum)

print(len(NOC_lt))

NOC_lt=sorted(NOC_lt,reverse=False)


for y in y_lt:
    dfii2 = df[df['Year'] == y]
    for j in top10_noc:
        dfii3=dfii2[dfii2["NOC"]==j]
        if not dfii3.empty:
            medal.extend(list(dfii3["Medal"]))
            host.extend(list(dfii3['Host']))
            Par.extend(list(dfii3['Par']))
            PerMedal.extend(list(dfii3['PerMedal']))
            year.append(y)
            NOC.append(j)
            DOM.extend(list(dfii3['Dom']))
            PerGold.extend(list(dfii3['PerGold']))

    for j in NOC_lt:
        dfii4=dfii2[dfii2["NOC"]==j]
        if not dfii4.empty:
            medal.extend(list(dfii4["Medal"]))
            host.extend(list(dfii4['Host']))
            Par.extend(list(dfii4['Par']))
            PerMedal.extend(list(dfii4['PerMedal']))
            year.append(y)
            NOC.append(j)
            DOM.extend(list(dfii4['Dom']))
            PerGold.extend(list(dfii4['PerGold']))

data1={
    "Year":year,
    "NOC":NOC,
    "Medal":medal,
    "Host":host,
    "Par":Par,
    "PerMedal":PerMedal,
    "Dom":DOM,
    "PerGold":PerGold
}

dfout=pd.DataFrame(data1)

print(dfout)

dfout.to_excel('/Users/lxjarctane2/Desktop/arima_use.xlsx')




# dfi=df[df['Year']==2024]
#
# set_med=set(dfi['Medal'])
#
# list_med=list(set_med)
#
# list_med=sorted(list_med,reverse=True)
#
# my_host_lt=[]
# my_year_lt=[]
# my_noc_lt=[]
# my_medal_lt=[]
# my_par_lt=[]
#
# for i in range(0,10):
#     my_year_lt.append(2024)
# for i in range(0,10):
#     dfii=dfi[dfi['Medal']==list_med[i]]
#     my_host_lt.append(list(dfii['Host'])[0])
#     my_noc_lt.append(list(dfii["NOC"])[0])
#     my_par_lt.append(list(dfii['Par'])[0])
#     my_medal_lt.append(list(dfii['Medal'])[0])
#
# df2=dfi[dfi['Medal']==0]
#
# lt_med2=list(df2['Medal'])
# lt_host2=list(df2['Host'])
# lt_noc2=list(df2['NOC'])
# lt_year2=list(df2['Year'])
# lt_par2=list(df2['Par'])
#
# medali=my_medal_lt+lt_med2
# hosti=my_host_lt+lt_host2
# Pari=my_par_lt+lt_par2
# NOCi=my_noc_lt+lt_noc2
# yeari=my_year_lt+lt_year2
























