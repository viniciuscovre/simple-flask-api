from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from src.models import db
from src.api import get_app


app = get_app('config')

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
