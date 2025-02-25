import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel('/Users/lxjarctane2/Desktop/graphmaking_mainnoc.xlsx',sheet_name='Sheet1',engine='openpyxl')

lt1=list(df['predict1'])
lt2=list(df['predict2'])
lt3=list(df['predict3'])
lt4=list(df['predict4'])
lt5=list(df['predict5'])
lt6=list(df['predict6'])
lt7=list(df['predict7'])
lt_sum1=[]
lt_sum1.append(lt1)
lt_sum1.append(lt2)
lt_sum1.append(lt3)
lt_sum2=[]
lt_sum2.append(lt1)
lt_sum2.append(lt4)
lt_sum2.append(lt5)
lt_sum3=[]
lt_sum3.append(lt1)
lt_sum3.append(lt6)
lt_sum3.append(lt7)

lt_sum=[]
lt_sum.append(lt_sum1)
lt_sum.append(lt_sum2)
lt_sum.append(lt_sum3)

noc_lt=list(df['NOC'])
lb_lt=['raw','p=0.15','p=0.2']
name_lt=['PerMedal','Par','Dom']


for j in range(3):
    plt.figure(figsize=(10, 6))

    for i in range(3):
        plt.plot(noc_lt, lt_sum[j][i], label=f'{lb_lt[i]}', marker='*')

    plt.xticks(ticks=noc_lt)

    plt.legend(
        loc="upper left",  # 图例的位置相对于图像
        bbox_to_anchor=(1.05, 1),  # 图例框锚点 (x, y)，将图例放在图像右侧
        borderaxespad=0.  # 图例与坐标轴之间的距离
    )

    plt.title(f"{name_lt[j]} prediction with different p")
    plt.xlabel("NOC")
    plt.ylabel(f"{name_lt[j]} Prediction")

    plt.grid(True)

    plt.savefig(f"{name_lt[j]} flexibility analysis.png", bbox_inches="tight", dpi=300)
    plt.show()


























