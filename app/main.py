from flask import Flask, render_template_string

from app.controllers.balance_controller import init_app


def create_app():
    app = Flask(__name__)
    init_app(app)

    @app.route('/')
    def index():
        documentation = """
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 50px;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
            }
            h1 {
                font-size: 24px;
                color: #333;
                margin-bottom: 20px;
            }
            p {
                font-size: 16px;
                color: #666;
                line-height: 1.6;
            }
            pre {
                font-size: 14px;
                color: #666;
                background-color: #f5f5f5;
                padding: 10px;
            }
            code {
                font-size: 14px;
                color: #c7254e;
                background-color: #f9f2f4;
                padding: 2px 5px;
                border-radius: 3px;
            }
            a {
                color: #007bff;
                text-decoration: none;
            }
        </style>
        <div class="container">
            <h1>Este aplicativo é um sistema de gerenciamento de saldo de contas</h1>
            <p>Construído usando Flask, um framework web em Python. Ele fornece uma API RESTful para realizar operações como depósito, saque e transferência de fundos entre contas. Os usuários podem interagir com o sistema através de requisições HTTP, permitindo-lhes criar contas, depositar e retirar fundos, bem como transferir dinheiro entre contas. O aplicativo também oferece endpoints para verificar o saldo das contas e redefinir o estado do sistema para fins de teste. Seu código-fonte é modular e bem estruturado, facilitando a expansão e manutenção futuras.</p>
        </div>
        """
        return render_template_string(documentation)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
