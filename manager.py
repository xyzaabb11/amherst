#!/usr/bin/env python
# encoding: utf-8


from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db

manager = Manager(app)

#manager.py migrate init --multidb
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
   manager.run()
