from flask import Blueprint, jsonify, request

from ..models.event import Event
from ..services.balance_service import BalanceService

# Cria uma instância do serviço de balanceamento
balance_service = BalanceService()

# Cria um blueprint(componentes modulares e reutilizáveis) para os endpoints relacionados ao saldo
balance_bp = Blueprint('balance', __name__)


#------------------------------------------------------------------------------------------------------------
# Endpoint para obter o saldo de uma conta específica
@balance_bp.route('/balance', methods=['GET'])
def get_balance():

    # Obtém o ID da conta da query string da requisição
    account_id = request.args.get('account_id')
    # Obtém o saldo da conta com o ID especificado
    balance = balance_service.get_balance(account_id)
    # Verifica se a conta existe e retorna o saldo ou retorna 0 e 404 caso contrário
    if balance is None:
        return '0', 404  # Retorna 404 e 0 como texto simples
    return str(balance), 200  # Retorna o saldo como texto simples com status 200


#------------------------------------------------------------------------------------------------------------
# Endpoint para processar eventos que alteram o saldo
@balance_bp.route('/event', methods=['POST'])
def post_event():
    # Obtém os dados JSON da requisição
    data = request.get_json()

    # Extrai os dados necessários do JSON
    event_type = data.get('type')
    amount = data.get('amount')
    destination = data.get('destination')
    origin = data.get('origin')

    # Verifica se os dados de entrada são válidos
    if event_type not in ['deposit', 'withdraw', 'transfer'] or not isinstance(amount, (int, float)):
        return jsonify({"error": "Invalid input"}), 400


    # Cria um objeto Event com os dados da requisição
    event = Event(event_type, amount, destination=destination, origin=origin)
    # Processa o evento no serviço de balanceamento
    response = balance_service.process_event(event)
    
    # Verifica se a resposta é nula (operação inválida)
    if response is None:
        # Retorna 404 e 0 para saques e transferências, caso contrário, retorna erro 400
        if event_type == 'withdraw' or event_type == 'transfer':
            return '0', 404  # Retorna 404 e 0 como texto simples
        return jsonify({"error": "Invalid event"}), 400

    # Retorna a resposta como JSON e status 201
    return jsonify(response), 201


#------------------------------------------------------------------------------------------------------------
# Endpoint para resetar o estado do serviço
@balance_bp.route('/reset', methods=['POST'])
def reset():
    print('Endpoint /reset chamado')
    balance_service.reset()
    return 'OK', 200

def init_app(app):
    app.register_blueprint(balance_bp)