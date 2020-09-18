import functools
import os

import flask


def access_required(route_func):
    @functools.wraps(route_func)
    def decorator(*args, **kwargs):
        if os.getenv('flask_token'):
            if 'token' in flask.request.cookies:
                token = flask.request.cookies['token']
                if token == os.getenv('flask_token'):
                    return route_func(*args, **kwargs)
        return flask.redirect('/auth')

    return decorator
