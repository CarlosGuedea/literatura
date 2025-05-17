from sqlalchemy import text
from app import db

def get_posts():
    query = text("""
        SELECT posts.id, posts.title, posts.content, posts.created_at, posts.genero_id, posts.user_id,
            users.username AS author
        FROM posts
        JOIN users ON posts.user_id = users.id
        ORDER BY posts.id DESC;
    """)
    result = db.session.execute(query)
    return result.mappings().all()

def create_post(user_id, title, content, genero_id):
    query = text("INSERT INTO posts (user_id, title, content, genero_id) VALUES (:user_id, :title, :content, :genero_id)")
    db.session.execute(query, {'user_id': user_id, 'title': title, 'content': content, 'genero_id': genero_id})
    db.session.commit()


def get_post_by_id(post_id):
    query = text("""
        SELECT posts.id, posts.title, posts.content, posts.user_id, posts.created_at,
               users.username AS author
        FROM posts
        JOIN users ON posts.user_id = users.id
        WHERE posts.id = :post_id
    """)
    result = db.session.execute(query, {'post_id': post_id})
    return result.mappings().first()  # Regresa un solo post o None


def get_posts_by_user(user_id):
    query = text("""
        SELECT posts.id, posts.title, posts.content, posts.created_at,
               posts.user_id,
               users.username AS author
        FROM posts
        JOIN users ON posts.user_id = users.id
        WHERE posts.user_id = :user_id
    """)
    result = db.session.execute(query, {'user_id': user_id})
    return result.mappings().all()



