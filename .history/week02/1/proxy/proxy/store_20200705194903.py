# 保存数据到MySQL数据库
import pymysql

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'xxx',
    'password' : 'xxxxx',
    'db' : 'python_learning'
}


class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls

        # self.run()

    def run(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()

class StoreInfo:
    def __init__(self):
        pass
    def store(self, sqls):
        db = ConnDB(dbInfo, sqls)
        db.run()
        