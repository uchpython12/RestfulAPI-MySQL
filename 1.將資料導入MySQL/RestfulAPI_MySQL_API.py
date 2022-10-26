try:
 import MySQLdb                    # pip install MySQL-python
except:
 import pymysql as MySQLdb         #  pip install MySQLdb
import pandas as pd                # pip install pandas


#創建表單  TEXT接受陣列表頭內容 例如 : TEXT=["value01","value02","value03"]
def MySQL_CREATE_TABLE(host,user,passwd,db,port=3306,tableName="",content=""):

    db = MySQLdb.connect(port=port,host=host, user=user, passwd=passwd, db=db)
    cursor = db.cursor()

    #將接收到的表頭欄位陣列 轉換SQL字串連接
    TEXTStr = ""
    for i in range(len(content)):
        TEXTStr = TEXTStr + content[i] + " TEXT,"
    print(TEXTStr)

    sql= "CREATE TABLE `"+tableName+"` (`id` INT(255) AUTO_INCREMENT , "+TEXTStr+" PRIMARY KEY (`id`))   "
    cursor.execute(sql)
    db.commit()

# 新增
def MySQL_insert(host,user,passwd,db,port=3306,tableName="",content="",VALUES=""):
    db = MySQLdb.connect(port=port,host=host, user=user, passwd=passwd, db=db)
    cursor = db.cursor()

    #將接收到的表頭欄位陣列 轉換SQL字串連接
    TEXTStr = ""
    VALUES_Str=""
    for i in range(len(content)-1):
        TEXTStr = TEXTStr +content[i]+" ,"
        VALUES_Str = VALUES_Str +"'"+VALUES[i]+"'"+" ,"

    TEXTStr = TEXTStr + content[len(content)-1]
    VALUES_Str = VALUES_Str + "'"+VALUES[len(content)-1]+"'"
    print("TEXTStr",TEXTStr)
    print("VALUES_Str=",VALUES_Str)
    sql="INSERT INTO `"+tableName+"`("+TEXTStr+") VALUES ("+VALUES_Str+")"
    try:
        cursor.execute(sql)
        print("新增成功")
    except :
        print("新增失敗")
    db.commit()

def MySQL_select(host,user,passwd,db,port=3306,tableName=""):
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db,port=port)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM "+tableName+"")
    result = cursor.fetchall()
    for record in result:
        str1=""
        for key in record:
            str1=str1+str(key)+" "
        print(str1)
# 將xlsx 轉成csv
def xlsx_to_csv(xlsx):
    df = pd.read_excel(xlsx+".xlsx")
    df.to_csv(xlsx+".csv")


