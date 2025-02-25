# 登录 得到cookie
# 带着cookie 请求书架url

# 必须把上面两个操作连起来
# 可以使用session请求 session会认为是一连串请求，整个过程cookie不丢失

import requests
import time

session=requests.Session()

data={
    "loginName": "13669939225",
    "password": "lxj17k133",
    "rememberMe":1
}

headers = {

    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",

    "Referer": "https://www.17k.com/",

    "Origin": "https://www.17k.com"

}



# 1.登录
url="https://passport.17k.com/ck/user/login"
resp=session.post(url,data=data,headers=headers)
# print(resp.text)
print(resp.cookies)

# 2760829817389049832068356ead088f407bdac5eb674be453839bf2c8c497



# 2.拿书架上的数据

params = {
    "page": 1,
    "appKey": "2406394919",
    "_": int(time.time() * 1000)
    # 可能需要时间戳参数 "_": int(time.time()*1000)
}


resp=session.get('https://user.17k.com/ck/author2/shelf',headers=headers,params=params)

print(resp.text)


# resp=requests.get('https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919',headers={"Cookie":'GUID=38a65f92-9354-419a-bc7d-1e3bb280377b; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; Hm_lvt_9793f42b498361373512340937deb2a0=1738902178,1738903945; HMACCOUNT=D1BF7C5C99E823B3; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F05%252F05%252F12%252F103991205.jpg-88x88%253Fv%253D1738903077000%26id%3D103991205%26nickname%3D%25E4%25B9%25A6%25E5%258F%258Bgor12hxq2%26e%3D1754456471%26s%3Ddc829e357abd39d1; tfstk=gTcma54R_usBdTidD0PXdTKFZw98cZN_FcCTX5EwUur7XEZYDVoiS2yausoxElmrqoPTMjdiIuP4CxETDlVi5DYJvBdKlqN_MHKp9eHcbxPQuGrVX8Wz-54qECBeMqN__3pI5gsqlD-hZgc4_UVzSP5a_1oaUzr75PS47s8ozuZz7rPNg7RzSrXabcPwr4r775zq_wt8Dorsa3fCYi_sVIkTo-qEuoux7bS4Utguq1fiZYm_YCql_1luo4dGWB52tukxQjFrg3STa2M-0zVHsN4oK4P4ocOCGSuEzAymsdQQfY0rp8D5kEaoi2cg-8JNXlenajFjEHfLYYgZs8uXx9a-Q2hxImK5_oHnz02KwgCLajmmg8VF4GWPLTi11z8tZO6_3zauv409fwJji-2JrUXUo-z7u_LkrOM83zauvUYlLEe4Pr5R.; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22103991205%22%2C%22%24device_id%22%3A%22194dea5877f603-057c94faa0a39c-1d525636-1484784-194dea587802260%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2238a65f92-9354-419a-bc7d-1e3bb280377b%22%7D; acw_sc__v2=67a59398521240e5886c1aacbe9c7052fb3a1c86; ssxmod_itna=eui=PAxGxmxUx4l+xCrrO2hqQqD5GCW3CDgilRDj2TqGNwYDZDiqAPGhDC3RKaObw4w3B8Y5=PK00PAWUCGDhdeGDraPWbT+DAoDhx7QDox0=DnxAQDjExYGGnxBYDQxAYDGDDpyDGLV8ExDdBPH1gca8vZc8BxGWEaKDmpKDROoDSWBsx+HHqG5DiaoDXrYDaaKDucH8hxi8D79LEoozD7ppf/3Epxi3UY5Em40O18F7WjvsDIIXr0h4Ue1eD2idP=D5qeR4CA44rnh4q0+560xqfLUYNArc0LiAfWDHqYD; ssxmod_itna2=eui=PAxGxmxUx4l+xCrrO2hqQqD5GCW3CDgilRDj2qA6FN+xD/FlDFx2ltI7IT2=D6GG2=KGI270iKBB07IwhNw3n7xC+BlMKEkCB8Yy6xzWiwrhhGDxFcjxKPKKCWeq5eeSjL55ARroiwiL2GrDc5ttxKH46BTtKYqCDKhKUvaa3v1Z2nWlgy8hc5zG8c8U1+vBoevGGD436ILkDI4VBILCA8WS=e5w+MXHx3CQaQTqGi+/2DzxMOtMgY+Wd=GF9vrVb8iK1KUYQahMg0Q5Qm3aR5uqpiw3hqrQ2HixcIjU+HGCiYpzozU8=cwiBYTkMKYnagxQSLb/2spfo4CtPW8rWTfLT/rYv4wid3xhhrMzpOCuBk8kNy3p5ozfnz3lKtADUCNz0pOWvYbmDkp=nk=QebdYqGqfAPD7jxD4Fiws6tI0+RBn7evE4mkiaiQDDjKDeTx4D===; Hm_lpvt_9793f42b498361373512340937deb2a0=1738905819'})
# 这是替代方法，手动登录网页端后，不用session方法，直接requests 请求 加入带有页面cookie的请求头 即可访问
# print(resp.text)
























