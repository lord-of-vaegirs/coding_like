import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.cm import get_cmap

from test_prac_graphmaking import img_height

df=pd.read_excel('/Users/lxjarctane2/Desktop/2024input.xlsx',sheet_name="Sheet1",engine='openpyxl')

df2=pd.read_excel('/Users/lxjarctane2/Desktop/2028data.xlsx',sheet_name='Sheet1',engine='openpyxl')

lt_noc=['AUS','CHN','ESP','FRA','GBR','GER','ITA','JPN','NED','NZL','USA']


value_list=[]

id=0
for i in lt_noc:
    value_list.append([])

    value_list[id].append(i)

    dfi=df[df['NOC']==i]
    value_list[id].extend(list(dfi['Total']))

    dfi2=df2[df2['NOC']==i]
    value_list[id].extend(list(dfi2['predict']))

    value_list[id].append(value_list[id][2]-value_list[id][1])

    id+=1

value_list.sort(key=lambda x: x[2],reverse=True)

# print(value_list)

mid=list(value_list[0])

left_b=value_list[1::2]
right=value_list[2::2]
left=left_b[-1::-1]

final_lt=[]
final_lt.extend(left)
final_lt.append([])
final_lt[-1]=mid
final_lt.extend(right)


print(final_lt)
final_medal_val=[]
final_noc_val=[]


for i in range(0,11):
    final_medal_val.append(final_lt[i][2])
    final_noc_val.append(final_lt[i][0])

noc_lt=[]
medal_24_lt=[]
medal_28_lt=[]

# print(value_list)

for i in value_list:
    noc_lt.append(i[0])
    medal_24_lt.append(i[1])
    medal_28_lt.append(i[2])

x=np.arange(len(lt_noc))

bar_width=0.4

fig,ax=plt.subplots(figsize=(8,5))
bar1=ax.barh(x-bar_width/2,medal_28_lt,height=bar_width,label='2028 medal',color='#FF9966')
bar2=ax.barh(x+bar_width/2,medal_24_lt,height=bar_width,label='2024 medal',color='#FF6666')


for i in [bar1,bar2]:
    for bar in i:
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
                str(int(bar.get_width())), va='center', ha='left', fontsize=10)

ax.set_title('2024-2028 Olympics Medal Contrast (Predicted Version)',fontsize=16)
ax.set_ylabel('NOC',fontsize=12)
ax.set_xlabel('Medals',fontsize=12)
ax.set_yticks(x)
ax.set_yticklabels(noc_lt)

ax.legend(fontsize=10)

plt.tight_layout()
plt.show()


# bg_img_path='/Users/lxjarctane2/Desktop/WechatIMG1286.jpg'
# bg_img=mpimg.imread(bg_img_path)
# img_height,img_width,_=bg_img.shape
#
#
#
#
# fig,ax=plt.subplots(figsize=(img_width/100,img_height/100))
#
# offset=0.5
# ax.imshow(bg_img,extent=(-offset,len(final_noc_val)+1,0,max(final_medal_val)+15),zorder=0,aspect='auto')
#
#
# x=np.arange(len(final_noc_val))
#
# colors=['red' if i in range(len(left)-1,len(left)+2) else 'lightblue' for i in range(len(final_noc_val))]
#
#
# ax.bar(x,final_medal_val,color=colors,edgecolor='black',linewidth=1.2,zorder=1)
# ax.set_xticks(x)
# ax.set_xticklabels(final_noc_val,fontsize=10,ha='center',color='black')
# ax.set_title('2028 Predicted Medal Stage',fontsize=16,color='black',pad=20)
# ax.set_ylabel('medal',fontsize=12,color='black')
# ax.set_xlabel('NOC',fontsize=12,color='black')
#
# for i in range(len(final_noc_val)):
#     ax.text(float(x[i]), final_medal_val[i] + 1, f'{round(final_medal_val[i])}', ha='center', fontsize=10,color='black',zorder=2)
#
# ax.set_xlim(-0.5, len(final_noc_val) - 0.5)
# ax.set_ylim(0, max(final_medal_val) + 10)
#
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
#
# plt.tight_layout()
# plt.show()





























