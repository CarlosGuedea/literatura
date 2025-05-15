from sqlalchemy import text
from app import db

def get_comments():
    query = text("""
        SELECT comments.id, comments.comment, comments.created_at,
               comments.author_name, posts.title AS post_title
        FROM comments
        JOIN posts ON comments.post_id = posts.id
    """)
    result = db.session.execute(query)
    return result.mappings().all()

def create_comment(post_id, author_name, comment):
    query = text("INSERT INTO comments (post_id, author_name, comment) VALUES (:post_id, :author_name, :comment)")
    db.session.execute(query, {
        'post_id': post_id,
        'author_name': author_name,
        'comment': comment
    })
    db.session.commit()
