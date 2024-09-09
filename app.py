from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS

from model import init_db
from route.customer_route import CustomerRoute

info = Info(title="Customer API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Inicializando o banco de dados
init_db()

# Registrando as rotas
CustomerRoute().init_routes(app)

