import os
from pydantic import BaseConfig


class Config(BaseConfig):
    mysql_host: str = "mysql"
    mysql_username: str = "root"
    mysql_password: str = os.environ.get("MYSQL_ROOT_PASSWORD", "password")
    mysql_database: str = os.environ.get("MYSQL_DATABASE", "app")
    session_cache_dir: str = "__cache__"
    session_lifetime: int = 24 * 60 * 60
