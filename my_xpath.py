#  xpath是在xml文档里面搜索内容的一门语言
# html 是 xml 一个子集

"""
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <author>
        <nick>周大强</nick>
        <nick>周芷若</nick>
    </author>
</book>

节点之间存在父子关系
"""
from lxml import etree
# etree.XML().xpath()
xml="""
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10085">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>惹了</nick>
        </div>
    </author>
    
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""
tree=etree.XML(xml) # 解析XML源码
# 还可以etree直接打开html文件
# tree=etree.parse("xxx.html")
# res=tree.xpath("/book")  # /表示层级关系 第一个/表示根节点
result=tree.xpath("/book/name/text()") # 像路径一样写出,父子节点都得写出来 最后想要文本的显示，只需将其改成text()即可
print(result)

# /book/author//nick/text() 中间两个/在一起表示省略了中间层级，直接到nick层
# /book/author/*/nick/text() 中间的*表示通配符 这层可以是任意节点

res2=tree.xpath("/book/*/nick/text()")
print(res2)

# xpath 里面多个同名标签 用中括号[]索引取得 注意从1开始
# 多个同名标签想取其中之一 还可以通过索引标签的属性 [@val="xxx"]

# xpath 相对查找： 搜索过一遍得到子标签的迭代对象后，在子标签下继续搜索，可以用
# 子标签.xpath("./xxx/yyy/text()")

# 想拿到某个标签里面属性的值 可以：
# /label/@val

# 还可以到网页里面->检查->element 点击左上角的箭头 将光标浮在想要看的内容上 对应的html代码就会在element里面出现，直接右键->copy->copy Xpath
















