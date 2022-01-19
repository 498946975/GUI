import pymysql


class DB(object):
    def __init__(self):
        self.username = "root"
        self.password = "123"
        self.host = "172.16.120.44"
        self.post = 3306
        self.db_name = "test_fastapi"
        self.sql_list = list()
        self.dbready = self.db_connect()

    def db_connect(self):
        db = pymysql.connect(
            host=self.host, user=self.username, password=self.password, database=self.db_name, port=self.post,
            charset='utf8'
        )
        return db

    def db_cursor(self):
        return self.dbready.cursor()

    def db_release(self):
        self.dbready.close()

    def get_all_users(self):
        sql = """
        SELECT
            id,
            username,
            dep_id,
            state,
            last_login_date,
            ip,
            is_delete,
            create_time 
        FROM
	        `user`"""
        self.sql_list.append(sql)
        cursor = self.db_cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        self.db_release()
        return data


if __name__ == '__main__':
    a = DB().get_all_users()
    print(a)
