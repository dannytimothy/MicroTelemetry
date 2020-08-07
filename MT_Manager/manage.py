<<<<<<< HEAD
# manage.py


import sys

=======
# manage.py hello
>>>>>>> 946728926bd1a01e520deeb8acc06dc29087bff6
from flask.cli import FlaskGroup

from project import create_app, db   
from project.api.models import User 


app = create_app()  
cli = FlaskGroup(create_app=create_app) 


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__'