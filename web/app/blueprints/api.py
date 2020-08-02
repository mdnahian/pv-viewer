from flask import Blueprint, jsonify

import core

api = Blueprint('api', __name__)

# Persistent Volume

@api.route('/pv', methods=['GET'])
def get_pv_all():
    all_pv = core.get_pv_all()
    return jsonify({'total': len(all_pv), 'resources': all_pv})


# Files

@api.route('/files/<pv_name>', methods=['POST'])
def get_files_from_pv(pv_name):
    pass

@api.route('/files/<pv_name>', methods=['DELETE'])
def delete_files_from_pv(pv_name):
    pass

