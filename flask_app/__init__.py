# from db.base import Base
from flask_api import FlaskAPI

flask_app = FlaskAPI(__name__)

flask_app.config['DEFAULT_PARSERS'] = [
    # 'flask.ext.api.parsers.JSONParser',
    # 'flask.ext.api.parsers.URLEncodedParser',
    'flask_api.parsers.MultiPartParser'
]

flask_app.config.from_pyfile('app_config.cfg')


__all__ = (flask_app,)