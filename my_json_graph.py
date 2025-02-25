"""
json是各个编程语言间通用的数据格式
准确说他就是字典转换成字符串格式 或者内嵌字典的列表转换成字符串格式

转化
import json
先准备符合json格式要求的python数据
data=[{k1:v1},{k2:v2},...]
通过json.dump(data)方法将py数据转化成json数据
data=json.dumps(data)
通过json.loads(data)方法将json转化成python数据
data=json.loads(data)



"""
import json
data=[{'你好':12},{'cpp':24}]
json_str=json.dumps(data,ensure_ascii=False) # ensure_ascii=False 可以保证中文输出
print(json_str)
print(type(json_str))
# json本质上就是字符串

dat2='{"python":12,"cpp":24}'
lt2=json.loads(dat2)
print(lt2)
print(type(lt2))
# 转化回来就是dict或者list形式






