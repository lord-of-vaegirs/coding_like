# 线程池： 一次性开辟一些线程，用户直接给线程池子提交任务，线程任务的调度交给线程池来完成
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import requests
import csv

f=open('xinfadi_vege_price.csv',mode="a",encoding='utf-8')
csvwriter=csv.writer(f)

# def fn(name):
#     for i in range(1000):
#         print(name,i)
#
#
# if __name__=='__main__':
#     # 创建线程池
#     with ThreadPoolExecutor(50) as t:
#         for i in range(100):
#             t.submit(fn,name=f'线程{i}')
#     # 等待线程池中任务全部执行完毕才会出来（守护线程）
#     # 进程池就是把上面的ThreadPoolExecutor换成ProcessPoolExecutor
#     print("123")

header={
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}


def download_one_page(url,data):
    resp=requests.post(url,headers=header,data=data)
    # print(resp.text)
    data=resp.json()
    lt=data["list"]
    for i in lt:
        name=i["prodName"]
        lowprice=i["lowPrice"]
        highprice=i["highPrice"]
        avgprice=i["avgPrice"]
        place=i["place"]
        csvwriter.writerow([name,lowprice,highprice,avgprice,place])

dat={
    "current":1,
    "limit":20
}



if __name__=='__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1,400):
            dat['current']=i
            t.submit(download_one_page,url="http://www.xinfadi.com.cn/getPriceData.html",data=dat)








"""
{
"current":1,
"limit":20,
"count":505709,
"list":[
        {
            "id":1738710,
            "prodName":"大白菜",
            "prodCatid":1186,
            "prodCat":"蔬菜",
            "prodPcatid":null,
            "prodPcat":"",
            "lowPrice":"0.55",
            "highPrice":"0.6",
            "avgPrice":"0.58",
            "place":"冀鲁豫鄂",
            "specInfo":"",
            "unitInfo":"斤",
            "pubDate":"2025-02-08 00:00:00",
            "status":null,
            "userIdCreate":138,
            "userIdModified":null,
            "userCreate":"admin",
            "userModified":null,
            "gmtCreate":null,
            "gmtModified":null
        },
        {
            "id":1738709,"prodName":"娃娃菜","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"1.2","highPrice":"1.5","avgPrice":"1.35","place":"豫鄂","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738708,"prodName":"小白菜","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"1.0","highPrice":"1.3","avgPrice":"1.15","place":"冀","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738707,"prodName":"圆白菜","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"0.8","highPrice":"2.2","avgPrice":"1.5","place":"冀鄂鲁","specInfo":"甘蓝","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738706,"prodName":"紫甘蓝","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"2.3","highPrice":"2.4","avgPrice":"2.35","place":"冀苏","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738705,"prodName":"芹菜","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"0.9","highPrice":"1.2","avgPrice":"1.05","place":"鲁","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738704,"prodName":"西芹","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"1.8","highPrice":"2.0","avgPrice":"1.9","place":"鲁辽","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738703,"prodName":"菠菜","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"1.0","highPrice":"1.5","avgPrice":"1.25","place":"鲁冀豫","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738702,"prodName":"莴笋","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"1.4","highPrice":"1.8","avgPrice":"1.6","place":"皖鲁浙闽","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738701,"prodName":"团生菜","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"2.0","highPrice":"3.5","avgPrice":"2.75","place":"云冀","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738700,"prodName":"罗马生菜","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"2.8","highPrice":"4.0","avgPrice":"3.4","place":"云","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738699,"prodName":"散叶生菜","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"2.2","highPrice":"2.3","avgPrice":"2.25","place":"辽冀京","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738698,"prodName":"油菜","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"1.0","highPrice":"1.5","avgPrice":"1.25","place":"皖川京鲁","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738697,"prodName":"香菜","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"2.5","highPrice":"2.8","avgPrice":"2.65","place":"冀","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738696,"prodName":"茴香","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"2.0","highPrice":"2.5","avgPrice":"2.25","place":"冀","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738695,"prodName":"韭菜","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"2.8","highPrice":"4.0","avgPrice":"3.4","place":"冀粤","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738694,"prodName":"苦菊","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"4.0","highPrice":"4.2","avgPrice":"4.1","place":"辽冀","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738693,"prodName":"油麦菜","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"2.0","highPrice":"3.0","avgPrice":"2.5","place":"京冀","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738692,"prodName":"散菜花","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"1.5","highPrice":"3.5","avgPrice":"2.5","place":"陕云鄂闽","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null},{"id":1738691,"prodName":"绿菜花","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"1.9","highPrice":"2.3","avgPrice":"2.1","place":"苏鄂浙","specInfo":"","unitInfo":"斤","pubDate":"2025-02-08 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null}]}


"""








