from xml.etree import ElementTree
import urllib.request as httplib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context  # 因.urlopen發生問題，將ssl憑證排除

######### 由網路下載 JSON 的 字串
url = "http://127.0.0.1:8080/xml"
req = httplib.Request(url, data=None,
                      headers={
                          'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"})
reponse = httplib.urlopen(req)  # 開啟連線動作
if reponse.code == 200:  # 當連線正常時
    contents = reponse.read()  # 讀取網頁內容
    contents = contents.decode("utf-8")  # 轉換編碼為 utf-8
    # print(contents)
    # 儲存檔案
    with open("iris.xml", "w", encoding="utf-8") as f:
        f.write(contents)

# 加载XML文件
root = ElementTree.fromstring(contents)
# XML 解析
row_value01 = root.findall("item/id")
row_value02 = root.findall("item/SepalLengthCm")
row_value03 = root.findall("item/SepalWidthCm")
row_value04 = root.findall("item/PetalLengthCm")
row_value05 = root.findall("item/PetalWidthCm")
row_value06 = root.findall("item/Species")
for x in range(len(row_value01)):
    str1 = " id:" + row_value01[x].text + \
           " SepalLengthCm:" + row_value02[x].text + \
           " SepalWidthCm:" + row_value03[x].text + \
           " PetalLengthCm:" + row_value04[x].text + \
           " PetalWidthCm:" + row_value05[x].text + \
           " Species:" + row_value06[x].text
    print(str1)

