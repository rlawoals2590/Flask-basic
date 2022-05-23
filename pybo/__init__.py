from venv import create
from flask import Flask

def create_app():
    app = Flask(__name__)

    from views import main_views
    app.register_blueprint(main_views.bp)
        
    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)
create_app()
               



