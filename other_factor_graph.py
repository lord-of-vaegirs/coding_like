import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_excel('/Users/lxjarctane2/Desktop/其它因素表.xlsx',sheet_name="Sheet1",engine='openpyxl')

df.dropna(inplace=True)

df.info()

noc_lt=list(df['NOC'])

gdp_lt=list(df['GDP(thousand billion dollar)'])

rate_lt=list(df['rate'])

x=np.arange(len(noc_lt))

bar_width=0.4

fig,ax=plt.subplots(figsize=(8,5))
bar1=ax.barh(x-bar_width/2,gdp_lt,height=bar_width,label='gdp',color='#ADD8E6')

for i in [bar1]:
    for bar in i:
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
                str(float(bar.get_width())), va='center', ha='left', fontsize=10)

ax.set_title('Other Factor(GDP Version)',fontsize=16)
ax.set_ylabel('NOC',fontsize=12)
ax.set_xlabel('GDP',fontsize=12)
ax.set_yticks(x)
ax.set_yticklabels(noc_lt)

ax.legend(fontsize=10)

plt.tight_layout()
plt.show()


fig,ax=plt.subplots(figsize=(8,5))
bar2=ax.barh(x+bar_width/2,rate_lt,height=bar_width,label='rate',color='#B0C4DE')

for i in [bar2]:
    for bar in i:
        ax.text(bar.get_width() + 0.002, bar.get_y() + bar.get_height() / 2,
                str(float(bar.get_width())), va='center', ha='left', fontsize=10)

ax.set_title('Other Factor(Rate Version)',fontsize=16)
ax.set_ylabel('NOC',fontsize=12)
ax.set_xlabel('rate',fontsize=12)
ax.set_yticks(x)
ax.set_yticklabels(noc_lt)

ax.legend(fontsize=10)

plt.tight_layout()
plt.show()