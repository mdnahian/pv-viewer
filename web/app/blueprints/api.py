from flask import Blueprint

api = Blueprint('api', 'api', url_prefix='/api')

# Persistent Volume

api.route('/pv', methods=['GET'])
def get_pv_all():
    pass

api.route('/pv/<pv_name>', methods=['GET'])
def get_pv_details(pv_name):
    pass


# Files

api.route('/files/<pv_name>', methods=['POST'])
def get_files_from_pv(pv_name):
    pass

api.route('/files/<pv_name>', methods=['DELETE'])
def delete_files_from_pv(pv_name):
    pass

