from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from Timezone import Timezone
from Timezones import Timezones
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

CORS(app, resources={r'/api/*': {'origins': '*'}})

@app.route('/')
def home():
    return 'Welcome to Timezones API'

api.add_resource(Timezones, '/api/timezones/')
api.add_resource(Timezone, '/api/timezones/<int:timezoneId>')

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Timezones API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
app.run(host='0.0.0.0', debug=True)