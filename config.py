#!/usr/bin/env python
# encoding: utf-8


SECRET_KEY = 'key'

#数据库配置
import os
basedir = os.path.abspath(os.path.dirname(__file__))
#SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'app.db')
SQLALCHEMY_BINDS = {
    'auth': 'mysql+pymysql://root:33848452ll.@127.0.0.1:3306/auth',
    'amblog': 'mysql+pymysql://root:33848452ll.@127.0.0.1:3306/amblog',
}
