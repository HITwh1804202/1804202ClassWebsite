"""
注册全部路由函数
"""
from rear.blueprints import test


def register_all_blueprints(app):
    # http://xx.com/test
    # GET：用于测试
    # POST：用于测试
    app.register_blueprint(test.test_bp, url_prefix='/test')
