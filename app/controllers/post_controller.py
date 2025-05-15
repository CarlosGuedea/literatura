from sqlalchemy import text
from app import db

def get_posts():
    query = text("""
        SELECT posts.id, posts.title, posts.content, posts.created_at,
               users.username AS author
        FROM posts
        JOIN users ON posts.user_id = users.id
    """)
    result = db.session.execute(query)
    return result.mappings().all()

def create_post(user_id, title, content):
    query = text("INSERT INTO posts (user_id, title, content) VALUES (:user_id, :title, :content)")
    db.session.execute(query, {'user_id': user_id, 'title': title, 'content': content})
    db.session.commit()
