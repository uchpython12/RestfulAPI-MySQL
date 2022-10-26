########## 由網路下載資料
import urllib.request as httplib  # 3.x
import json

######### 由網路下載 JSON 的 字串
url="http://127.0.0.1:8080/json"
req = httplib.Request( url,data=None,
    headers={ 'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"})
reponse = httplib.urlopen(req)               # 開啟連線動作
if reponse.code==200:                        # 當連線正常時
    contents=reponse.read()                  # 讀取網頁內容
    contents=contents.decode("utf-8")        # 轉換編碼為 utf-8
    # print(contents)
    # 儲存檔案
    with open("iris.json", "w", encoding="utf-8") as f:
        f.write(contents)


######### 字串 換成  JSON 的 Dict
obj1= json.loads(contents)

# print(obj1[0]) # id 0 第一列

for x in obj1:
    str1=" id:"+str(x['id'])+\
         " SepalLengthCm:"+str(x['SepalLengthCm'])+\
         " SepalWidthCm:"+str(x['SepalWidthCm'])+\
         " PetalLengthCm:"+str(x['PetalLengthCm'])+\
         " PetalWidthCm:"+str(x['PetalWidthCm'])+\
         " Species:"+str(x['Species'])
    print(str1)

