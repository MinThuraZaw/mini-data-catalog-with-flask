from flask import Flask
from blueprints.main import main_bp
from blueprints.settings import settings_bp
from blueprints.api import api_bp
from blueprints.db import close_db


app = Flask(__name__)

app.register_blueprint(main_bp)
app.register_blueprint(settings_bp)
app.register_blueprint(api_bp, url_prefix='/api')



@app.teardown_appcontext
def teardown_db(exception):
    close_db()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)