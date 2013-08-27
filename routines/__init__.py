#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
