import json
from json import JSONDecodeError


class PostHandler:
    def __init__(self, path):
        self.path = path

    def load_posts(self):
        posts = []
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts = json.load(file)
        except JSONDecodeError:
            return posts, 'Error loading data from JSON'

        return posts, None

    def search_post(self, search_substring):
        posts = []
        load_posts, error = self.load_posts()
        for post in load_posts:
            if search_substring.lower() in post['content'].lower():
                posts.append(post)
        return posts, error

    def save_post_to_json(self, posts):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(posts, file)

    def add_post(self, post):
        posts, error = self.load_posts()
        posts.append(post)
        self.save_post_to_json(posts)
