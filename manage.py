from app import app
from flask_migrate import Migrate


migrate = Migrate(app, app.db)

if __name__ == "__main__":
    app.run()