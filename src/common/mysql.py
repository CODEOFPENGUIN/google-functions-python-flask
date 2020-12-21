import pymysql.cursors
import os
from common.logger import *
from common.custom_exception import CustomException

log = getLogger(__name__)

class MysqlManager:
    def __init__(self):
        # connection 정보
        self.conn = pymysql.connect(
            host = 'localhost' if not os.environ.get("CLOUD_SQL_HOST") else os.environ.get("CLOUD_SQL_HOST"),
            user = 'root' if not os.environ.get("CLOUD_SQL_USER") else os.environ.get("CLOUD_SQL_USER"),
            password = 'localdb' if not os.environ.get("CLOUD_SQL_PASSWORD") else os.environ.get("CLOUD_SQL_PASSWORD"),
            db = 'sample' if not os.environ.get("CLOUD_SQL_DB") else os.environ.get("CLOUD_SQL_DB"),
            charset = 'utf8mb4')
    def __enter__(self):
        return self
    def selectAll(self, sql, args=None):
        """
        @sql : Query String
        @args : Query Arguments(tuple, list or dict) - optional
        return list
        """
        try:
            with self.conn.cursor() as cursor:
                if args != None :
                    cursor.execute(sql, args)
                else:
                    cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            log.error(e)
            return CustomException(str(e))
    def selectOne(self, sql, args=None):
        """
        @sql : Query String
        @args : Query Arguments(tuple, list or dict) - optional
        return dict
        """
        try:
            with self.conn.cursor() as cursor:
                if args != None :
                    cursor.execute(sql, args)
                else:
                    cursor.execute(sql)
                return cursor.fetchone()
        except Exception as e:
            log.error(e)
            return CustomException(str(e))
    def executeData(self, sql, args=None):
        """
        @sql : Query String
        @args : Query Arguments(tuple, list or dict) - optional
        return int
        """
        result = -1
        try:
            with self.conn.cursor() as cursor:
                if args != None :
                    result = cursor.execute(sql, args)
                else:
                    result = cursor.execute(sql)
        except Exception as e:
            log.error(e)
            self.conn.rollback()
            return CustomException(str(e))
        finally:
            self.conn.commit()
        return result
    def __exit__(self, type, value, traceback):
        self.conn.close()
        return self