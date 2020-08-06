# manage.py hello
from flask.cli import FlaskGroup
from project import app

#Invoke CLI
cli = FlaskGroup(app)


if __name__ == '__main__'