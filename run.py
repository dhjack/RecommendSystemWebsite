#!/usr/bin/python
# -*- coding: utf-8 -*-


from web import app as application
application.config.from_object('web.default_settings')
application.config.from_pyfile('settings.cfg', silent=True)

application.run(host='0.0.0.0', ssl_context='adhoc')
