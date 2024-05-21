from flask import Flask, jsonify, render_template_string, request

from app.controllers.balance_controller import init_app


def create_app():
    app = Flask(__name__)
    init_app(app)

    @app.route('/')
    def index():
        documentation = """
        <h1>EBANX Software Engineer Take-home assignment</h1>
        <p>This API provides endpoints to manage account balances.</p>
        
        <h2>Endpoints</h2>
        
        <h3>Reset State</h3>
        <p><b>POST /reset</b></p>
        <p>Resets the state of the service.</p>
        
        <h3>Get Balance</h3>
        <p><b>GET /balance?account_id=ID</b></p>
        <p>Returns the balance of the account with the specified ID.</p>
        <p>Example Response for existing account (HTTP 200): <code>20</code></p>
        <p>Example Response for non-existing account (HTTP 404): <code>0</code></p>
        
        <h3>Process Event</h3>
        <p><b>POST /event</b></p>
        <p>Processes an event that alters the balance of an account.</p>
        <p>Request Body:</p>
        <pre>
        {
          "type": "deposit" | "withdraw" | "transfer",
          "destination": "account_id",  // required for "deposit" and "transfer"
          "origin": "account_id",       // required for "withdraw" and "transfer"
          "amount": number
        }
        </pre>
        <p>Example Response for deposit (HTTP 201): <code>{"destination": {"id": "100", "balance": 10}}</code></p>
        <p>Example Response for withdraw (HTTP 201): <code>{"origin": {"id": "100", "balance": 5}}</code></p>
        <p>Example Response for transfer (HTTP 201): <code>{"origin": {"id": "100", "balance": 0}, "destination": {"id": "300", "balance": 15}}</code></p>
        <p>Example Response for invalid operation (HTTP 404): <code>0</code></p>
        
        <h2>How to test the API</h2>
        <p>Use tools like <a href="https://www.postman.com/" target="_blank">Postman</a> to send HTTP requests to the API endpoints and verify the responses.</p>
        
        <h2>Notes</h2>
        <p>Ensure the server is running before sending requests. Use <code>python -m app.main</code> to start the server.</p>
        """
        return render_template_string(documentation)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
