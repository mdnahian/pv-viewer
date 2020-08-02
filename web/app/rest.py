import sys
sys.path.append('/opt/pvviewer/lib/web/app')
import uuid
from flask import Flask, jsonify

from blueprints.api import api

main = Flask(__name__)
main.config['SECRET_KEY'] = uuid.uuid4().hex
main.url_map.strict_slashes = False

def build_error_response(err):
    try:
        return {"error": {"type": str(err.name), "message": str(err)}}
    except:
        return {"error": {"type": str(err.__class__.__name__), "message": str(err)}}

@main.errorhandler(Exception)
def main_error(err):
    e = build_error_response(err)
    response = jsonify(e)
    try:
        response.status_code = err.code
    except:
        response.status_code = 500
    return response

@main.route('/alive')
def get_app_alive():
    return jsonify({})

@main.route('/ready')
def get_app_ready():
    return jsonify({})

main.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    main.run(host='0.0.0.0', port=8080, debug=True)