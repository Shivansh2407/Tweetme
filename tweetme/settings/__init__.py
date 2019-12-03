from .base import *

if 'DATABASE_URL' in os.environ:  # in Heroku's environment
    from .production import *
else:
    from .local import *
