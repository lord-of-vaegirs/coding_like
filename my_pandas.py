"""
pandas

手册： htts://www.pypandas.cn/docs/

df= pd.read_excel(“name.xlsx”,sheet_name='sheet1',engine='openpyxl') 读取excel表格数据
openpyxl 是一个新的库 得import进来
上面这行代码用于读取Excel表格文件

df.head() 查看前五行的数据
如果改变（）里面 的数可以改变查看的行数
例： df.head(10)

被剔除的值 在这里显示的时候就是nan

info() 查看数据（表格文件）的信息

以下面这个文件为例
<class 'pandas.core.frame.DataFrame'> 文件数据类型
RangeIndex: 15 entries, 0 to 14  有15行数据
Data columns (total 4 columns): 这是对表格的解释
    第一列         有数据的行       类型
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   Unnamed: 0  15 non-null     object
 1   成本          15 non-null     int64
 2   售价          15 non-null     int64
 3   利润          15 non-null     int64
dtypes: int64(3), object(1) 各个类型出现次数
memory usage: 612.0+ bytes  内存大小
None

缺失值处理
dropna()函数 去除含缺失值的行

更改列的数据类型：例 df['column']=df['column'].astype(float)

选择和过滤：
df[df['column']==1] 在原本key的位置放置条件式 使其变成筛选功能 最后打印true或者false

可以通过3sigma原则筛选数据
如：
lb=df['column'].mean()-3*df['column'].std()
ub=df['column'].mean()+3*df['column'].std()
print(df[(df['column']>=lb) & (df['column']<=ub)])

字典格式的数据
可以通过pd.DataFrame(data) 来转换成表格格式


"""
# import numpy as np
# import pandas as pd
#
# import openpyxl
#
# df= pd.read_excel('/Users/lxjarctane2/Downloads/price.xlsx',sheet_name='Sheet1',engine='openpyxl') # 读取excel表格数据
#
# print(df.head(10))
#
# print(df.info())
#
# df=df.dropna()
#
# print(df.head(10))
#
# df['利润']=df['利润'].astype(float)
#
# print(df.info())
#
# lb=df['利润'].mean()-3*df['利润'].std()
# ub=df['利润'].mean()+3*df['利润'].std()
#
# selected_df=df[(df['利润']>=lb) & (df['利润']<=ub)]
# print(selected_df)
# print(selected_df.info())
#
#
# arr=np.array([1,3,4])
# data={'样本号':[1,2,3],'萼片长(cm)':[8.9,2.1,4.5],'类型_num':[0,0,1]}
# dataf=pd.DataFrame(data)
# print(dataf)

import numpy as np
import pandas as pd

data={
    '姓名':['张三','李四','王五','老六','赵七'],
    '身高':[175 for i in range(5)],
    '体重':[50 for j in range(5)],
    '成绩':np.random.randint(40,90,5)
}

df=pd.DataFrame(data)

print(df)

print(df[df['成绩']==max(df['成绩'])])

print(np.mean(df['成绩']))

dff=df[df['成绩']<60]

print(dff['姓名'])










