from __future__ import absolute_import
from dj.commands.dj import dj

if __name__ == '__main__':
    try:
        dj()
    except SystemExit as e:
        if e.code:
            raise
