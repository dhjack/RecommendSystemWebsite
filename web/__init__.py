#!/usr/bin/python
# -*- coding: utf-8 -*-  

import os
from flask import Flask

app = Flask(__name__ ,instance_relative_config=True)

import views

if __name__ == '__main__':
    pass
    #app.run(host='0.0.0.0')
