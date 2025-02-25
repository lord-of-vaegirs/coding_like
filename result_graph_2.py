import matplotlib.pyplot as plt
from cycler import cycler
import pandas as pd

df=pd.read_excel('/Users/lxjarctane2/Desktop/arima_use.xlsx',sheet_name='Sheet1',engine='openpyxl')

df2=pd.read_excel('/Users/lxjarctane2/Desktop/result_arima_transpose.xlsx',sheet_name='Sheet1',engine="openpyxl")

df2.dropna()

df.info()

df2.info()

lt_noc=['AUS','CHN','ESP','FRA','GBR','GER','ITA','JPN','NED','NZL','USA']

dict_noc={}
for i in lt_noc:
    dict_noc[i]=[[],[],[]] # Par PerMedal Dom


for i in lt_noc:
    dfi=df[df['NOC']==i]
    df2i=df2[df2['NOC']==i]
    dict_noc[i][0].extend(list(dfi['Par'])[-1::-1])
    dict_noc[i][0].extend(list(df2i['Par']))
    dict_noc[i][1].extend(list(dfi['PerMedal'])[-1::-1])
    dict_noc[i][1].extend(list(df2i['PerMedal']))
    dict_noc[i][2].extend(list(dfi['Dom'])[-1::-1])
    dict_noc[i][2].extend(list(df2i['Dom']))

custom_colors = [
    "#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00",
    "#ffff33", "#a65628", "#f781bf", "#999999", "#66c2a5", "#fc8d62"
]

print(dict_noc)

y_lt=[]
for j in range(1996,2029,4):
    y_lt.append(j)

col=['Par','PerMedal','Dom']
print(y_lt)

for i in range(0,3):
    plt.figure(figsize=(10,6))

    plt.rcParams["axes.prop_cycle"] = cycler(color=custom_colors)
    for j in lt_noc:
        line,=plt.plot(y_lt,dict_noc[j][i],label=f'{j} {col[i]} line',marker='o')
        line_color=line.get_color()
        plt.text(2028, dict_noc[j][i][8], f'2028{j}', ha='left',fontsize=6,color=line_color)

    plt.xticks(ticks=y_lt)

    plt.legend(
        loc="upper left",  # 图例的位置相对于图像
        bbox_to_anchor=(1.05, 1),  # 图例框锚点 (x, y)，将图例放在图像右侧
        borderaxespad=0.  # 图例与坐标轴之间的距离
    )

    plt.title(f"{col[i]} 1996-2028 sum_linemap")
    plt.xlabel("Year")
    plt.ylabel(f"{col[i]}")

    plt.grid(True)

    plt.savefig(f"{col[i]} 1996-2028 sum_linemap.png", bbox_inches="tight", dpi=300)
    plt.show()








