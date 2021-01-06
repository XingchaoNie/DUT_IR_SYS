"""
@ encoding:utf-8
@ author:nxc
@ GitHub:
@ 建立语料数据库
@ MySQL.mysearchdb.WordSpace(user:root,password:12345678)
@ 代码仅用于学习
"""

import pandas as pd
import pymysql
import numpy as np
import jieba


class MySQLData:
    def __init__(self):
        self.db_user = "root"
        self.db_password = "12345678"
        self.db_name = "mySearchDB"
        self.my_csv_data = np.array(pd.read_csv("searchData.csv", encoding='utf-8'))
        self.db = pymysql.connect("localhost", self.db_user, self.db_password, self.db_name)
        print("DB connect!")

    def down_connect(self):
        self.db.close()
        print("DB down!")

    def init_my_sql(self):
        cur = self.db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS WorkSpace(Id INT PRIMARY KEY AUTO_INCREMENT,Link VARCHAR(100),Name VARCHAR(50),Summary VARCHAR(500),Type VARCHAR(15),Time VARCHAR(10))")
        [r, c] = np.shape(self.my_csv_data)
        for i in range(r):
            print(i)
            Link = self.my_csv_data[i, 0]
            Name = str(self.my_csv_data[i, 1]).replace("'", "")
            Summary = str(self.my_csv_data[i, 2]).replace("'", "")
            Type = self.my_csv_data[i, 3]
            Time = self.my_csv_data[i, 4]
            cur.execute("INSERT INTO WorkSpace Values("+str(i+1)+",'"+str(Link)+"','"+str(Name)+"','"+str(Summary)+"','"+str(Type)+"','"+str(Time)+"')")
            self.db.commit()
        print("set MySql Done!")

    def search(self, message):
        cur = self.db.cursor()
        sql = "SELECT * FROM WorkSpace WHERE Name LIKE '%" + message + "%'"
        cur.execute(sql)
        returnList = cur.fetchall()
        return returnList


def main():
    my_data_sql = MySQLData()
    my_data_sql.init_my_sql()               # 初始化语料数据库
    my_data_sql.down_connect()


if __name__ == '__main__':
    main()

