__author__ = "Jonathan Enzinna <jonnyfunfun@gmail.com>"
__version__ = "0.0.1"

import threading


class Routine(object):
    def __init__(self, recurrence):
        self.schedule = recurrence

    def __call__(self, orig_func):
        decorator_self = self

        def wrap(*args, **kwargs):
            ev = threading.Event()

            def loop():
                while not ev.wait(decorator_self.schedule):
                    orig_func(*args, **kwargs)

            thread = threading.Thread(target=loop)
            thread.daemon = True
            thread.start()

            return ev

        return wrap