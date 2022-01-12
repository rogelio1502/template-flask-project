from flask import Flask, render_template
from flask_migrate import Migrate

from models.module import db

from routes.module_blueprint import module_blueprint

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(module_blueprint, url_prefix='/module')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()

