"""
测试
"""

from flask import Blueprint, request, jsonify


test_bp = Blueprint("test_bp", __name__)


@test_bp.route('', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return 'Hello World'
    elif request.method == 'POST':
        rev_json = request.get_json(silent=True)
        name = rev_json.get('name')
        print('Hello ' + name)
        return jsonify(data="post successfully")