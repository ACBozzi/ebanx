from flask import Flask


def create_app():

    #instância do Flask
    app = Flask(__name__)

    #importando os controladores
    with app.app_context():
        from .controllers import balance_controller

        return app