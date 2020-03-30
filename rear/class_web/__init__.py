from flask import Flask
import os
import click

from class_web.extensions import db
from class_web.settings import config
from class_web.common.register_all_blueprints import register_all_blueprints


def make_app(config_name=None):
    """
    app的工厂函数
    :param config_name:
    :return: app
    """
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('hitapply')
    app.config.from_object(config[config_name])

    # 为app注册相关信息
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):
    """
    注册扩展组件
    :param app:
    :return:
    """
    db.init_app(app)


def register_commands(app):
    """
    注册命令行
    :param app:
    :return:
    """
    @app.cli.command()
    def initdb():
        db.create_all()
        click.echo('Initialized database.')


def register_blueprints(app):
    register_all_blueprints(app)