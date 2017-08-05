

import sys
sys.path.insert(0, '/var/www/RecommendSystemWebsite')

from web import app as application
application.config.from_object('web.default_settings')
application.config.from_pyfile('settings.cfg', silent=True)
