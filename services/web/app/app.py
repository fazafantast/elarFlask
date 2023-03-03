import os
from flask import Flask, render_template
from flask_migrate import Migrate

from models import db

app = Flask(__name__, template_folder='templates')

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f'postgresql+psycopg2://{os.environ["PG_USER"]}:{os.environ["PG_USER_PASSWORD"]}'
    f'@{os.environ["POSTGRES_HOST"]}/{os.environ["POSTGRES_DB"]}'
)
db.init_app(app)
migrate = Migrate(app, db)
migrate.init_app(app, db)


@app.errorhandler(404)
def not_found(error):
    return render_template('page-not-found.html'), 404


if __name__ == '__main__':
    app.run()
    db.create_all()
