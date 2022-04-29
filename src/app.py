# Importaciones requeridad

from flask import Flask
from settings.database import mongo
from tasks.routes import tasks_bp 
from flask_cors import CORS

# Cargando clase de configuracion
from config import Config
app_config = Config()

# Iniciando app y Blueprints
app = Flask(__name__)

# Configurando BD
app.config["MONGO_URI"] = app_config.DATABASE_URL
mongo.init_app(app)
CORS(app)

# Registrando Blueprints
app.register_blueprint(tasks_bp, url_prefix='/tasks')

# Correr la aplicacion de flask
app.run(debug = True)