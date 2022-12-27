import logging

from flask import Blueprint, render_template, request
from lesson12_project.main.utils import PostHandler

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    search_substring = request.args.get('s')
    logging.info(f'Поиск: {search_substring}')
    post_handler = PostHandler('posts.json')
    posts, error = post_handler.search_post(search_substring)
    if error:
        logging.info(f'Ошибка: {error}')
        return 'Ошибка!'

    return render_template('post_list.html', posts=posts, search_substring=search_substring)
