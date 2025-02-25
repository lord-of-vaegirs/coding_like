import pandas as pd

df= pd.read_excel('/Users/lxjarctane2/Desktop/athlete.xlsx',sheet_name='Sheet1',engine='openpyxl')


df.dropna()


set_event=set(df['Event'])

list_event=list(set_event)

set_country=set(df['NOC'])

list_country=list(set_country)

set_year=set(df['Year'])

list_year=list(set_year)

list_year=sorted(list_year)

print(list_year)
# 1041 234 31

dic_ynoc=dict()

for i in list_year:
    dfi=df[df['Year']==i]
    a=set(dfi['Event'])
    len1=len(a)
    print(len1)
    dic_ynoc[i]=dict()
    for j in list_country:
        dffi=dfi[dfi['NOC']==j]
        b=set(dffi['Event'])
        len2=len(b)
        ratio=len2/len1
        dic_ynoc[i][j]=ratio


df2=pd.DataFrame(dic_ynoc)


df2.to_excel('/Users/lxjarctane2/Desktop/participantial_ratio.xlsx')






