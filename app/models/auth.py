from .abstract import AbstractModel

from hashlib import sha256


class AuthModel(AbstractModel):
    def __init__(self, config):
        super().__init__(config)

    def login(self, username, password):
        user = self.find_user_by_name_and_password(username, password)
        if not user:
            return False, None
        return True, user

    def create_user(self, username, password):
        hashed_password = self.hash_password(password)
        sql = "INSERT INTO users(username, password) VALUE (%s, %s);"
        self.execute(sql, username, hashed_password)

    def find_user_by_name_and_password(self, username, password):
        hashed_password = self.hash_password(password)
        sql = "SELECT * FROM users where username=%s AND password=%s"
        return self.fetch_one(sql, username, hashed_password)

    def logout(self):
        pass

    def hash_password(self, password: str):
        return sha256(password.encode()).hexdigest()
