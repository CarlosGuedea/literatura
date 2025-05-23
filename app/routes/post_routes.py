from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for
from app.controllers.post_controller import get_posts, create_post, get_post_by_id, get_posts_by_cuentos, get_posts_by_poesia, get_posts_by_cronica, delete_post_by_id
from flask_login import login_required
from app import db
from sqlalchemy import text

post_bp = Blueprint('post', __name__)

@post_bp.route('/posts_new', methods=['GET'])
@login_required
def new_post():
    return render_template('posts-new.html')

@post_bp.route('/posts', methods=['GET'])
def list_posts():
    posts = get_posts()
    return render_template('post_list.html', posts=posts)

@post_bp.route('/cuentos', methods=['GET'])
def list_cuentos():
    cuentos = get_posts_by_cuentos()
    return render_template('cuentos.html', cuentos=cuentos)

@post_bp.route('/poesias', methods=['GET'])
def list_poesias():
    poesias = get_posts_by_poesia()
    return render_template('poesias.html', poesias=poesias)

@post_bp.route('/cronicas', methods=['GET'])
def cronicas():
    cronicas = get_posts_by_cronica()
    return render_template('cronicas.html', cronicas=cronicas)

@post_bp.route('/posts', methods=['POST'])
@login_required
def add_post():
    data = request.json
    create_post(data['user_id'], data['title'], data['content'], data['genero_id'])
    return jsonify({'message': 'Post created'}), 201

@post_bp.route('/posts/<int:post_id>')
def show_post(post_id):
    post = get_post_by_id(post_id)
    if not post:
        return "Post no encontrado", 404
    return render_template('post_detail.html', post=post)


@post_bp.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    if 'user_id' not in session:
        return redirect(url_for('user.login'))

    post = get_post_by_id(post_id)

    if not post:
        return "Post no encontrado", 404

    if post['user_id'] != session['user_id']:
        return "No tienes permiso para editar este post", 403

    if request.method == 'POST':
        new_title = request.form['title']
        new_content = request.form['content']
        query = text("""
            UPDATE posts SET title = :title, content = :content WHERE id = :id
        """)
        db.session.execute(query, {
            'title': new_title,
            'content': new_content,
            'id': post_id
        })
        db.session.commit()
        return redirect(url_for('post.show_post', post_id=post_id))

    return render_template('post_edit.html', post=post)



@post_bp.route('/posts/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = get_post_by_id(post_id)
    if not post:
        return "Post no encontrado", 404

    if post['user_id'] != session.get('user_id'):
        return "No tienes permiso para eliminar este post", 403

    delete_post_by_id(post_id)
    return redirect(url_for('post.list_posts'))  # Ajusta a tu vista principal de posts
