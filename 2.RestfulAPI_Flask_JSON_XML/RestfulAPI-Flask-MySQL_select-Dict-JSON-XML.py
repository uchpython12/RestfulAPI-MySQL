# 測試 請透過 http://127.0.0.1:5000/
import dicttoxml
import flask     # pip install flask
import pymysql as MySQLdb  # pip install pymysql
import json

app = flask.Flask(__name__)


# 路徑設定  http://127.0.0.1:8080/
@app.route("/")
def fun1():                    # 函式設定 (路徑設定後的函式)
    html1="<a href='http://127.0.0.1:8080/xml'>xml</a><p>"+ \
           "<a href='http://127.0.0.1:8080/json'>json</a>"
    return html1


def 讀取資料庫():
    host = "localhost"
    user = "admin"
    passwd = "admin"
    db = "mydatabase"
    tableName = "iris"
    db = MySQLdb.connect(host=host,
                         user=user, passwd=passwd, db=db)
    cursor = db.cursor()
    所有欄位名稱 = []
    sql2 = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'" + tableName + "'ORDER BY ORDINAL_POSITION"
    cursor.execute(sql2)
    result = cursor.fetchall()
    for record in result:
        print(record)
        所有欄位名稱.append(record[3])  # 取欄位名稱

    print("欄位名稱:", 所有欄位名稱)

    cursor.execute("SELECT * FROM " + tableName)
    result = cursor.fetchall()

    array1 = []
    for i in result:
        dict1 = {}
        x = 0
        for 欄位名稱 in 所有欄位名稱:
            if 欄位名稱 == "進貨日期":
                dict1[欄位名稱] = i[x].strftime("%Y-%m-%d")
            else:
                dict1[欄位名稱] = i[x]
                x = x + 1

        print(dict1)
        array1.append(dict1)

    return array1

def 轉JSON(array1):
    print("資料庫的內容，轉成 Array dict1", array1)
    jsonstr = json.dumps(array1,ensure_ascii=False)
    print("dict1 轉成 JSON 的字串")
    print(jsonstr)
    f = open("dict1.json", "w", encoding="utf-8")
    f.write(jsonstr)
    f.close()
    return jsonstr


def arrayDictionary_XML(array1):
        str1 = ""
        for 筆 in array1:
            str3 = ""
            for k in 筆:
                for v in 筆[k]:
                    str2 = "<v1>v2</v1>"
                    str2 = str2.replace("v1", k)
                    str2 = str2.replace("v2", v)
                    str3 = str3 + str2
            str1 = str1 + "<row>" + str3 + "</row>"
        return '<?xml version="1.0" encoding="UTF-8"?><ROOT>' + str1 + '</ROOT>'


def 轉XML(array1):


    # XMLstr = arrayDictionary_XML(array1)
    # print("dict1 轉成 XML 的字串")
    # print(XMLstr)

    XMLstr = dicttoxml.dicttoxml(array1, custom_root='fruit').decode('utf-8')
    print("dict1 轉成 XML 的字串")
    print(XMLstr)

    # write to xml file
    f = open("dict1.xml", "w", encoding="utf-8")
    f.write(XMLstr)
    f.close()
    return XMLstr


#http://127.0.0.1/json
@app.route("/json")
def fun3():
    array1 =讀取資料庫()
    jonstr1=轉JSON(array1)
    return flask.Response(jonstr1, mimetype='text/json')


#http://127.0.0.1/xml
@app.route("/xml")
def fun4():
    array1 =讀取資料庫()
    xmlstr1=轉XML(array1)
    return flask.Response(xmlstr1, mimetype='text/xml')


if __name__ == '__main__':
    app.run(port=8080)