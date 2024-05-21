#controladores http

from flask import Blueprint, request, jsonify
from ..services.balance_service import BalanceService
from ..models.event import Event


# Cria um Blueprint para os endpoints relacionados ao saldo
balance_service = BalanceService()
balance_bp = Blueprint('balance', __name__)

@balance_bp.route('/balance', methods=['GET'])
def get_balance():
    # Endpoint para obter o saldo atual
    balance = balance_service.get_balance()
    return jsonify({"balance": balance})

@balance_bp.route('/event', methods=['POST'])
def post_event():
    # Endpoint para processar eventos que alteram o saldo
    data = request.get_json()
    event_type = data.get('type')
    amount = data.get('amount')

    # Verifica se os dados de entrada são válidos
    if event_type not in ['credit', 'debit'] or not isinstance(amount, (int, float)):
        return jsonify({"error": "Invalid input"}), 400

    # Cria um objeto Event e processa o evento
    event = Event(event_type, amount)
    balance_service.process_event(event)
    return jsonify({"message": "Event processed"}), 200

def init_app(app):
    #registra
    app.register_blueprint(balance_bp)