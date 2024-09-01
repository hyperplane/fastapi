from typing import List, Dict
import pymysql.cursors

from app.configs import Config


class AbstractModel(object):
    def __init__(self, config: Config):
        self.connection = pymysql.connect(
            host=config.mysql_host,
            user=config.mysql_username,
            password=config.mysql_password,
            database=config.mysql_database,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def fetch_all(self, sql_statement: str, *args: any) -> List[Dict[str, any]]:
        with self.connection.cursor() as cursor:
            self._execute(sql_statement, cursor, *args)
            return cursor.fetchall()

    def fetch_one(self, sql_statement, *args) -> Dict[str, any]:
        with self.connection.cursor() as cursor:
            self._execute(sql_statement, cursor, *args)
            return cursor.fetchone()

    def execute(self, sql_statement, *args) -> None:
        with self.connection.cursor() as cursor:
            self._execute(sql_statement, cursor, *args)

    def _execute(self, sql_statement: str, cursor: pymysql.connections.Cursor, *args: any) -> None:
        cursor.execute(sql_statement, args)

    def __del__(self):
        self.connection.close()
