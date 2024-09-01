from app.models.abstract import AbstractModel


class ArticleModel(AbstractModel):
    def __init__(self, config):
        super(ArticleModel, self).__init__(config)

    def fetch_recent_articles(self, limit=5):
        sql = "SELECT * FROM articles ORDER BY created_at DESC LIMIT %s"
        return self.fetch_all(sql, limit)

    def fetch_article_by_id(self, article_id):
        sql = "SELECT * FROM articles INNER JOIN users u on articles.user_id = u.id WHERE articles.id=%s"
        return self.fetch_one(sql, article_id)

    def create_article(self, user_id, title, body):
        sql = "INSERT INTO articles(user_id, title, body) VALUE (%s, %s, %s);"
        self.execute(sql, user_id, title, body)
