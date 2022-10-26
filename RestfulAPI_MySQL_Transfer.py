import RestfulAPI_MySQL_API
import pandas as pd

host="localhost"
user="admin"
passwd="admin"
db="mydatabase"
tableName="iris"

df = pd.read_csv("Iris.csv")  # 讀取 Iris.csv

x = df[df.columns]  # 設定x的資料
x = x.to_numpy()  # y從 pandas 轉 numpy
print("資料筆數為", x.shape)
# x = x.reshape(x.shape)
print(x, "外型大小")  # 印出結果

"1.創建資料庫表(CREATE_TABLE)--------------------------------------------------------"
content=[] #欄位初始值
for i in range(1,len(df.columns)): #從 1開始 因為 Iris.csv id欄位 會自動創建 不需要在創建id欄位
    content.append(str(df.columns[i]))#創建 欄位名字初始值
# print(content)
# content=["value01","value02","value03"] #創建 欄位名字初始值

# 主機,帳號,密碼,資料庫名稱,資料庫表名稱,欄位名稱
RestfulAPI_MySQL_API.MySQL_CREATE_TABLE(host=host,
            user= user,passwd=passwd,db=db,tableName=tableName,content=content)

"2.新增資料數據(MySQL_insert)--------------------------------------------------------"
#將csv 資料讀取到陣列中
x_VALUES=[]
for i in range(len(x)):
    y_VALUES = []
    for j in range(1, len(x[i])):
        y_VALUES.append(str(x[i][j]))
    x_VALUES.append(y_VALUES)
print(x_VALUES)
#將抓取到的資料新增到MySQL
for i in range(len(x)):
    RestfulAPI_MySQL_API.MySQL_insert(host=host,
                 user=user,passwd=passwd,db=db,tableName=tableName,content=content,VALUES=x_VALUES[i])
