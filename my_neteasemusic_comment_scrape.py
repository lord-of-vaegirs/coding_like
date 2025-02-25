# 1.找到未加密的参数 浏览器 检查 network XHR
# 找get开头和评论有关的
# 点开调用堆栈 找到最上方的core代码 进入
# 找到send语句行  打开右侧local 看requests下的url 是否是comment 不是的话就往下走换栈
# 直到看到comment resource
# 找到的位置往下看 delete语句下方bfJ4N语句 把断点设在跳过它的地方，
# e2x.data语句这行设置断点可以看到e2x i2x(未加密数据)
# 再找bfJ4N是如何被赋值的，靠的是window.asrsea 再搜索这个 找到类似下面注释的几个函数在一起的语句块 就是加密过程了
# 2.想办法把参数进行加密（必须参考网易的逻辑）
# 3.请求到网易，拿到评论信息

import os
# os.environ['PY_SSIZE_T_CLEAN'] = '1'
from Crypto.Cipher import  AES
from base64 import b64encode
import  requests
import json as js
import csv

url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token=6383de70a7538580e1c3e08e20408f11"

# 30ccb467852f8d77c9882328e769d9d7024ce2f96dd6dd0351d01330f87908d2e855513101bd57a7cbd6a159607743e8b058002beb52f88cc526a42a4fecd27176d088e6635f77b27af1859fe57f7245ef3c12c732de253d5054d8cabe41f070b2e24bdccfafc6a0ce52c6a2fe861755fdd49f8fadabde9419b571a777fa988e

# q8EbOqN6WYAmb40RU+5VloO44UT09xBtbIOcAPCPsyE1eVUiwinCbtjatIqRBCZXuNCugJx5XrU6q+Ik9viXBCAraEtiGr1+5+GKBiAEw2YnFyTLdQj+uiHS12o3paPo01lGb4l6WiXYFk42433hSrrWAQ9ipAC+sMNfCuRMTLWCpP7/Ha7LTZTWEMHX0i0YP2Dk+eQz+9ANeAYzOi+xR3vLhrpnflAX7JHrO3vNZQlWe6RPftQdESCgqkBfzVQBGEZWdl0q57mdoJXI3f+SkgD0wMSJDqRByCy5cuHglRts8Fx1XJk0dALrgF5OSkMayLcAwhpnmxYgY2n2LzQILTIVshnguwGVh3oHEoaxkFc=


"""
网易加密的过程
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) { # a是要加密的内容
        var c = CryptoJS.enc.Utf8.parse(b) # 密钥 （g和i）
          , d = CryptoJS.enc.Utf8.parse("0102030405060708") # iv偏移量
          , e = CryptoJS.enc.Utf8.parse(a)  # e是数据
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d, # 偏移量
            mode: CryptoJS.mode.CBC  #  模式是CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) { # d是数据 e f g 固定
        var h = {}
          , i = a(16); # 生成16位随机种子
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),  # 最后 efg被钉死 i在下面被我固定了一个16位随机种子   encSecKey 唯一生成
        h 
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d, # 执行上方d函数
    window.ecnonasr = e

"""


"""
数据
i2x:
csrf_token
: 
"6383de70a7538580e1c3e08e20408f11"
cursor
: 
"-1"
offset
: 
"0"
orderType
: 
"1"
pageNo
: 
"1"
pageSize
: 
"20"
rid
: 
"R_SO_4_2668124242"
threadId
: 
"R_SO_4_2668124242"

"""


# i: "nEmfjii3ZHL0acFz"  i是function a 里面生成的16位随机种子
# e f g 钉死了

i="nEmfjii3ZHL0acFz"
f="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g="0CoJUm6Qyw8W8jud"
e="010001"

# encSecKey="5bb77223a0bba149e1e401e7cd349f836cbecdba19a4d76f4642b8e2e4c6e5640d8cf457d9e71280ec44fd24a245c935a7a064486642447754db0c0c263ce622c6c7e02170acacbd272d432b5aa868d1f5553f693f7b14bb972ee620a89d827b4de37bb2a7e951163ca1c157284a5a0b19e32f7200e6522dfe9f1163a9ae9bf2"
# encText="bplLeAHTm6cOLxbxXlLgTPxoYgWNvSTIXAog11TeUOZhm6lHJRPFPdOU8xrKPyFaZVICsPG5YwRIdzIPyPZFiIB86xslcQFh6q7qy6JecF4XJ1gGWlYRfgGg7rzzfXxN"

# encSecKey 每次唯一生成 只与i即16位随机种子变化有关
# encText 做了两次加密

data={
    "csrf_token": "6383de70a7538580e1c3e08e20408f11",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_2668124242",
    "threadId": "R_SO_4_2668124242"
}


def get_encSecKey(): # 既然参数都定好了 直接返回结果即可
    return "5bb77223a0bba149e1e401e7cd349f836cbecdba19a4d76f4642b8e2e4c6e5640d8cf457d9e71280ec44fd24a245c935a7a064486642447754db0c0c263ce622c6c7e02170acacbd272d432b5aa868d1f5553f693f7b14bb972ee620a89d827b4de37bb2a7e951163ca1c157284a5a0b19e32f7200e6522dfe9f1163a9ae9bf2"

def get_params(data): # 模拟d函数确定encText 默认收到字符串
    first=enc_params(data,g) # 第一次加密
    second=enc_params(first,i) # 第二次加密
    return second

def to_16(data):
    pad=16-len(data)%16
    data+=chr(pad)*pad
    return data


def enc_params(data,key):
    iv="0102030405060708"
    data=to_16(data)
    aes=AES.new(key=key.encode('utf-8'),IV=iv.encode('utf-8'),mode=AES.MODE_CBC) # 创造加密工具
    bs=aes.encrypt(data.encode("utf-8")) # 加密内容长度得是16的倍数
    return str(b64encode(bs),'utf-8')  # bs为加密后的数据 但是得先转换成b64，才能再转换成utf-8，最后转换成string

resp=requests.post(url,data={
    "params":get_params(js.dumps(data)),
    "encSecKey":get_encSecKey()
})
# 请求参数缺params 和 encSecKey 得我们自己加密自己传的参数才行
# print(resp.text)
# print(type(resp.text))
res=resp.json()
data_lt=res["data"]["comments"]

fi=open('neteasemusic_comments.csv',mode="w",encoding='utf-8')
csvwriter=csv.writer(fi)


for i in data_lt:
    name=i['user']["nickname"]
    comments=i["content"]
    like=i['likedCount']
    reply=i["replyCount"]
    strres=f'{name}: {comments}'
    likestr=f'like: {like}'
    replystr=f'reply: {reply}'
    csvwriter.writerow([strres,likestr,replystr])

fi.close()







