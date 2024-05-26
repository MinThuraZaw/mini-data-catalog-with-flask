from flask import Flask
from blueprints.main import main_bp
from blueprints.settings import settings_bp

app = Flask(__name__)

app.register_blueprint(main_bp)
app.register_blueprint(settings_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)