from threading import Thread
import requests


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


def save_user(message, lang) -> int():
    post_data = {
        'tg_id': message.chat.id,
        'username': message.chat.username,
        'first_name': message.chat.first_name,
        'last_name': message.chat.last_name,
        'lang': lang,
    }
    x = requests.post(url='http://127.0.0.1:8000/user/register/', data=post_data)
    return x.status_code
